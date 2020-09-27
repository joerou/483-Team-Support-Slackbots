import os
import time
import hashlib
import hmac
from flask import Flask, request, jsonify
from slackeventsapi import SlackEventAdapter
from slack import WebClient

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/event", app)

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)

###############################################################################
# events handler
###############################################################################

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.chat_postMessage(channel=channel, text=message)


# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.chat_postMessage(channel=channel, text=text)


# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

###############################################################################
# slash commend handler
###############################################################################

# Validate if the requset is actually from slack
def validate_request():
    request_body = request.get_data().decode('utf-8')
    timestamp = request.headers['X-Slack-Request-Timestamp']
    if abs(time.time() - float(timestamp)) > 60 * 5:
        return False
    sig_basestring = 'v0:' + timestamp + ':' + request_body
    my_signature = 'v0=' + hmac.new(
        key=slack_signing_secret.encode('utf-8'),
        msg=sig_basestring.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    slack_signature = request.headers['X-Slack-Signature']
    if not hmac.compare_digest(my_signature, slack_signature):
        return False
    return True

# Sample slash commend "/hello"
@app.route('/slack/event/hello', methods=['POST'])
def hello():
    if validate_request():
        # return **must be implemented**
        # Send 'Hello!' to channel
        payload = {'response_type': 'in_channel', 'text': 'Hello!'}    
    else:
        payload = {'text': 'Bad Request'}
    return jsonify(payload)

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
# slack_events_adapter.start(port=3000)
app.run(port=3000)
