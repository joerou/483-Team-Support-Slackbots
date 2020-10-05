import os
import json
from flask import Flask, request, jsonify, make_response
from slackeventsapi import SlackEventAdapter
from slack import WebClient
from slack.signature import SignatureVerifier
from slack.errors import SlackApiError

# import time
# import hashlib
# import hmac


# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/event", app)
signature_verifier = SignatureVerifier(slack_signing_secret)

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)

###############################################################################
# events handler
###############################################################################

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.chat_postMessage(channel=channel, text=message)


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.chat_postMessage(channel=channel, text=text)



#Triggering event upon new member joining
@slack_events_adapter.on("member_joined_channel")
def new_member_survey(event_data):
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)
    event = event_data["event"]
    channel = event["channel"]
    user = event["user"]
    message = "Hello <@%s> Thanks for joining the chat! Please type /survey to take a quick personality survey:tada:" % user
    slack_client.chat_postMessage(channel=channel, text=message)
    



# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

###############################################################################
# slash commend handler
###############################################################################

# Use provided slack python api instead
# # Validate if the requset is actually from slack
# def validate_request():
#     request_body = request.get_data().decode('utf-8')
#     timestamp = request.headers['X-Slack-Request-Timestamp']
#     if abs(time.time() - float(timestamp)) > 60 * 5:
#         return False
#     sig_basestring = 'v0:' + timestamp + ':' + request_body
#     my_signature = 'v0=' + hmac.new(
#         key=slack_signing_secret.encode('utf-8'),
#         msg=sig_basestring.encode('utf-8'),
#         digestmod=hashlib.sha256
#     ).hexdigest()
#     slack_signature = request.headers['X-Slack-Signature']
#     if not hmac.compare_digest(my_signature, slack_signature):
#         return False
#     return True

# Sample slash commend "/hello"
@app.route('/slack/event/hello', methods=['POST'])
def hello():
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        # Send 'Hello!' to channel
        # use webClient methods
        channel = request.form['channel_id']
        slack_client.chat_postMessage(channel=channel, text='Hello!')
        return make_response("", 200)
        # Or return json
        payload = {'response_type': 'in_channel', 'text': 'Hello!'} 
    else:
        payload = {'text': 'Bad Request'}
    # return **must be implemented**
    return jsonify(payload)

# Sample slash commend "/sampleServey"
@app.route('/slack/event/sampleServey', methods=['POST'])
def sampleServey():
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)
    try:
        api_response = slack_client.views_open(
            trigger_id=request.form["trigger_id"],
            view={
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Sample Servey",
                    "emoji": True
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit",
                    "emoji": True
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel",
                    "emoji": True
                },
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Please select *True* _or_ *False*."
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "True",
                                    "emoji": True
                                },
                                "value": "True"
                            }
                        ]
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "False",
                                    "emoji": True
                                },
                                "value": "False"
                            }
                        ]
                    }
                ]
            }
        )
        return make_response("", 200)
    except SlackApiError as e:
        code = e.response["error"]
        return make_response(f"Failed to open a modal due to {code}", 200)
        
@app.route('/slack/event/Survey', methods=['POST'])
    def sampleServey():
        if not signature_verifier.is_valid_request(request.get_data(), request.headers):
            return make_response("invalid request", 403)
        try:
            api_response = slack_client.views_open(
                trigger_id=request.form["trigger_id"],
                view={
                    "type": "modal",
                    "title": {
                        "type": "plain_text",
                        "text": "Question 1",
                        "emoji": True
                        },
                    "submit": {
                        "type": "plain_text",
                        "text": "Next",
                        "emoji": True
                        },
                    "close": {
                        "type": "plain_text",
                        "text": "Cancel",
                        "emoji": True
                        },
                    "blocks": [
                            {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "Please Select a Number 1-5"
                                }
                            },
                            {
                            "type": "actions",
                            "elements": [
                                    {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "1",
                                        },
                                    "value": "1"
                                    }
                                ]
                            },
                            {
                            "type": "actions",
                            "elements": [
                                    {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "2",
                                        },
                                    "value": "2"
                                    },
                            {
                            "type": "actions",
                            "elements": [
                                    {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "3",
                                        },
                                    "value": "3"
                                    },
                            {
                            "type": "actions",
                            "elements": [
                                    {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "4",
                                        },
                                    "value": "4"
                                    },
                            {
                            "type": "actions",
                            "elements": [
                                    {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "5",
                                        },
                                    "value": "5"
                                    }
                                ]
                            }
                        ]
                    }
                )
            return make_response("", 200)
        except SlackApiError as e:
            code = e.response["error"]
            return make_response(f"Failed to open a modal due to {code}", 200)

###############################################################################

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == "__main__":
# slack_events_adapter.start(port=3000)
    app.run(port=3000)
