import logging
import os
from slack_bolt import App
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

# logging
logging.basicConfig(level=logging.DEBUG)
bolt_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
handler = SlackRequestHandler(bolt_app)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)
    
###############################################################################
# message handler
###############################################################################

# Listens to incoming messages that contain "hello"
@bolt_app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@bolt_app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

# # Example responder to greetings
# @slack_events_adapter.on("message")
# def handle_message(event_data):
#     message = event_data["event"]
#     # If the incoming message contains "hi", then respond with a "Hello" message
#     if message.get("subtype") is None and "hi" in message.get('text'):
#         channel = message["channel"]
#         message = "Hello <@%s>! :tada:" % message["user"]
#         slack_client.chat_postMessage(channel=channel, text=message)


# Example reaction emoji echo
@bolt_app.event("reaction_added")
def reaction_added(event, say):
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    say(channel=channel, text=text)



#Triggering event upon new member joining
@bolt_app.event("member_joined_channel")
def new_member_survey(event):
    channel = event["channel"]
    user = event["user"]
    message = "Hello <@%s> Thanks for joining the chat!, Please take a personality survey with /survey :tada:" % user
    say(channel=channel, text=message)



# Error events
@bolt_app.event("error")
def error_handler(err):
    print("ERROR: " + str(err))

###############################################################################
# slash command handler
###############################################################################

# Sample slash command "/hello"
@bolt_app.command('/hello')
def hello(ack, say):
    # Acknowledge command request
    ack()
    # Send 'Hello!' to channel
    say('Hello!')


# The echo command simply echoes on command
@bolt_app.command("/echo")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(f"{command['text']}")

# Sample slash command "/sampleservey"
@bolt_app.command('/sampleservey')
def sampleServey(ack, body):
    ack()
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
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
    except Exception as e:
        logger.error(f"Error opening modal: {e}")
        
        
#slash command for survey
@bolt_app.command('/servey')
def survey():
    ack()
    try:
        client.views_open(
            trigger_id=request.form["trigger_id"],
            view={
                    "blocks": [
                        {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "select",
                               },
                               {
                               "option_groups": [
                                    {
                                        "label": "I am the life of the party",
                                        "options": [
                                            {
                                                "label": "1",
                                                "value": "value-1"
                                                 },
                                            {
                                                "label": "2",
                                                "value": "value-2"
                                                    },
                                            {
                                                "label": "3",
                                                "value": "value-3"
                                                    },
                                            {
                                                "label": "4",
                                                "value": "value-4"
                                                    },
                                            {
                                                "label": "5",
                                                "value": "value-5"
                                                    }
                                            
                                        ]
                                     }
                               ]
                                     }
                        ]
                                               }
                    ]
                }
            )
    except Exception as e:
        logger.error(f"Error opening modal: {e}")

###############################################################################

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == "__main__":
# slack_events_adapter.start(port=3000)
    app.run(debug=True, port=int(os.environ.get("PORT", 3000)))
