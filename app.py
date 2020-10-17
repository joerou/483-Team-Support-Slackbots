import sys
import logging
import os
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from questions_payloads import *

###############################################################################
# Initializing
###############################################################################

# enable logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bolt
bolt_app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Initialize Flask app and bolt handler
app = Flask(__name__)
handler = SlackRequestHandler(bolt_app)

# redirect request to bolt
@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


# Create a logger for the 'azure' SDK and configure a console output
azureLogger = logging.getLogger('azure')
azureLogger.setLevel(logging.DEBUG)
azureLogger.addHandler(logging.StreamHandler(stream=sys.stdout))

# Initialize the Cosmos client
cosmos = CosmosClient(
    url=os.environ.get("AZURE_COSMOS_ENDPOINT"),
    credential=os.environ.get("AZURE_COSMOS_MASTER_KEY"),
    logging_enable=True
)

# Create a database
database_name = 'bot-storage'
database = cosmos.create_database_if_not_exists(id=database_name)

# Create a container
# Using a good partition key improves the performance of database operations.
msgDB_name = 'message-storage'
msgDB = database.create_container_if_not_exists(
    id=msgDB_name,
    partition_key=PartitionKey(path="/user"),
    offer_throughput=400
)

## Add more container here for survey

###############################################################################
# Middleware
###############################################################################

# Log request
@bolt_app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()

# Log all messages
@bolt_app.middleware
def log_message(payload, logger, next):
    if (payload["type"]=="message"):
        # id is required
        msg = {
            'id' : payload["ts"],
            'channel': payload["channel"],
            'user': payload["user"],
            'message': payload["text"],
            'mention': None
        }
        msgDB.create_item(msg)
    return next()

###############################################################################
# Message Handler
###############################################################################

# Listens to incoming messages that contain "hello"
@bolt_app.message("hello")
def message_hello(ack, message, say):
    # say() sends a message to the channel where the event was triggered
    ack()
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

# handle all messages
@bolt_app.message("")
def message_rest(ack):
    ack()

###############################################################################
# Action Handler
###############################################################################

@bolt_app.action("button_click")
def action_button_click(ack, body, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

@bolt_app.action("take_survey")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
            trigger_id=body["trigger_id"],
        # View payload
            view=question1_payload
    )
    
@bolt_app.action("question1_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question2_payload
    )

###############################################################################
# Event Handler
###############################################################################

# Example reaction emoji echo
@bolt_app.event("reaction_added")
def reaction_added(ack, event, say):
    ack()
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    say(channel=channel, text=text)

# Triggering event upon new member joining
@bolt_app.event("member_joined_channel")
def new_member_survey(ack, event, say):
    ack()
    user = event["user"]
    message = "Hello <@%s> Thanks for joining the chat!, Please take a personality survey by pressing the take survey button! :tada:" % user
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": message},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Take Survey"},
                    "action_id": "take_survey"
                }
            }
        ],
        text=message
    )

# Error events
@bolt_app.event("error")
def error_handler(ack, err):
    ack()
    print("ERROR: " + str(err))

###############################################################################
# Slash Command Handler
###############################################################################

# Sample slash command "/hello"
@bolt_app.command('/hello')
def hello(ack, say):
    # Acknowledge command request
    ack()
    # Send 'Hello!' to channel
    say('Hello!')


# The echo command simply echoes on command
@bolt_app.command('/echo')
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(f"{command['text']}")

# Sample slash command "/samplesurvey"
@bolt_app.command('/samplesurvey')
def sampleSurvey(ack, body, client, logger):
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
@bolt_app.command('/survey')
def survey(ack, body, client):
# Acknowledge the command request
    ack()
# Call views_open with the built-in client
    client.views_open(
    # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
    # View payload
        view={
            "type": "modal",
        # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "My App"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Click me!"},
                        "action_id": "button_abc"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_c",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }
)

###############################################################################

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 3000)))
