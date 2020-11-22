import sys
import logging
import os
import time
import json
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from questions_payloads import *

###############################################################################
# Initializing
###############################################################################
# initializing survey_dict
survey_dict = {}

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

## Start platform related code
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
survey_containter = database.get_container_client("survey-storage")
## Add more container here for survey

#Create Brainstorming container
brainDB_name = 'brainstorm-storage'
brainDB = database.create_container_if_not_exists(
    id=brainDB_name,
    partition_key=PartitionKey(path="/user"),
    offer_throughput=400
)

## The database usage in the rest part may need to be changed on a different platform
## End platform related code

# Global Variables

#Brainstorming Globals
brainstormOn = 0

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
def log_message(payload, next):
    global brainstormOn
    if ("type" in payload and payload["type"]=="message"):
        # id is required
        msg = {
            'id' : payload["ts"],
            'channel': payload["channel"],
            'user': payload["user"],
            'message': payload["text"],
            'mention': None
        }
        msgDB.create_item(msg)

        if (brainstormOn == 1):
            msgBrain = {
                'id' : payload["ts"],
                'channel': payload["channel"],
                'user': payload["user"],
                'message': payload["text"],
                'mention': None
            }
            brainDB.create_item(msgBrain)

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
# handler for a radio button being selected
@bolt_app.action("this_is_an_action_id")
def action_button_click(ack, body, client, say):
    # Acknowledge the action
    ack();
    form_json = json.loads(body)
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view={
                "type": "modal",
            # View identifier
                "callback_id": "view_1",
                "title": {"type": "plain_text", "text": "Question 1"},
                
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "hello %s" % (form_json['actions'][0]['selected_option']['value'])},
                        "accessory": {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "Next"},
                            "action_id": "question1_next"
                        }
                    },
                    {
                      "type": "section",
                      "text": {
                        "type": "plain_text",
                        "text": "Choose a number 1-5 based on how this represents you"
                      },
                      "accessory": {
                        "type": "radio_buttons",
                        "action_id": "this_is_an_action_id",
                        
                        "options": [
                          {
                            "value": "Q1_1",
                            "text": {
                              "type": "plain_text",
                              "text": "1 Strongly Disagree"
                              #"action_id": "this_is_an_action_id"
                            }
                          },
                          {
                            "value": "Q1_2",
                            "text": {
                              "type": "plain_text",
                              "text": "2"
                            }
                          },
                          {
                            "value": "Q1_3",
                            "text": {
                              "type": "plain_text",
                              "text": "3"
                            }
                          },
                          {
                            "value": "Q1_4",
                            "text": {
                              "type": "plain_text",
                              "text": "4"
                            }
                          },
                          {
                            "value": "Q1_5",
                            "text": {
                              "type": "plain_text",
                              "text": "5 Strongly Agree"
                            }
                          }
                        ]
                      }
                    }
                    
                    
                ]
            }

    )

    say('hello')
    user = body['user']['id']
    value = body['actions']['selected_option']['value']
    question = ""
    response = int(value[-1])
    for char in value:
        if char == "Q":
            pass
        elif char == "_":
            break
        else:
            question += char
            
    question = int(question)
    temp = survey_dict[user]
    temp[question] = response
    survey_dict[user] = temp
    
@bolt_app.action("EndBrainstorming")
def action_button_click(ack, body, say):
    # Acknowledge the action
    ack()
    global brainstormOn

    #Check if brainstorm bit is already 0 to prevent spamming of the button
    if (brainstormOn == 1):
        brainstormOn = 0
        say('Here are all of the ideas the group came up with: ')

        #iterate through all of the ideas the group proposed
        item_list = list(brainDB.read_all_items())
        msg = ""
        for i in item_list:
            msg += "• " + i.get("message") + "\n"
            brainDB.delete_item(item = i.get("id"), partition_key = i.get("user"))
        say(msg)
        say("Need a mockup of one of the ideas? Try using <https://www.sketchup.com/plans-and-pricing/sketchup-free|Google Sketch up> or <https://www.figma.com/|Figma>")
        say("Also a reminder has been set for next week to look back on the brainstorming process")
        
    else:
        say("Brainstorming has already ended")

@bolt_app.action("button_click")
def action_button_click(ack, body, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

@bolt_app.action("take_survey")
def action_button_click(ack, body, client):
    # Acknowledge the action
    user = body['user']['id']
    survey_dict[user] = [0 for x in range(50)]
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
    
@bolt_app.action("question2_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question3_payload
    )


@bolt_app.action("question3_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question4_payload
    )
    
@bolt_app.action("question4_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question5_payload
    )
    
@bolt_app.action("question5_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question6_payload
    )
    
@bolt_app.action("question6_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question7_payload
    )
    
@bolt_app.action("question7_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question8_payload
    )
    
@bolt_app.action("question8_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question9_payload
    )
    
@bolt_app.action("question9_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question10_payload
    )
    
@bolt_app.action("question10_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question11_payload
    )
    
@bolt_app.action("question11_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question12_payload
    )
    
@bolt_app.action("question12_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question13_payload
    )
    
@bolt_app.action("question13_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question14_payload
    )
    
@bolt_app.action("question14_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question15_payload
    )
    
@bolt_app.action("question15_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question16_payload
    )
    
@bolt_app.action("question16_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question17_payload
    )
    
@bolt_app.action("question17_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question18_payload
    )
    
@bolt_app.action("question18_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question19_payload
    )
    
@bolt_app.action("question19_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question20_payload
    )
    
@bolt_app.action("question20_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question21_payload
    )
    
@bolt_app.action("question21_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question22_payload
    )
    
@bolt_app.action("question22_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question23_payload
    )
    
@bolt_app.action("question23_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question24_payload
    )
    
@bolt_app.action("question24_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question25_payload
    )
    
@bolt_app.action("question25_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question26_payload
    )
    
@bolt_app.action("question26_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question27_payload
    )
    
@bolt_app.action("question27_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question28_payload
    )
    
@bolt_app.action("question28_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question29_payload
    )
    
@bolt_app.action("question29_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question30_payload
    )
    
@bolt_app.action("question30_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question31_payload
    )
    
@bolt_app.action("question31_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question32_payload
    )
    
@bolt_app.action("question32_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question33_payload
    )
    
@bolt_app.action("question33_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question34_payload
    )
    
@bolt_app.action("question34_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question35_payload
    )
    
@bolt_app.action("question35_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question36_payload
    )
    
@bolt_app.action("question36_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question37_payload
    )
    
@bolt_app.action("question37_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question38_payload
    )
    
@bolt_app.action("question38_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question39_payload
    )
    
@bolt_app.action("question39_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question40_payload
    )


@bolt_app.action("question40_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question41_payload
    )
    
@bolt_app.action("question41_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question42_payload
    )
    
@bolt_app.action("question42_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question43_payload
    )
    
@bolt_app.action("question43_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question44_payload
    )
    
@bolt_app.action("question44_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question45_payload
    )
    
@bolt_app.action("question45_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question46_payload
    )
    
@bolt_app.action("question46_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question47_payload
    )
    
@bolt_app.action("question47_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question48_payload
    )
    
@bolt_app.action("question48_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question49_payload
    )
    
@bolt_app.action("question49_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=question50_payload
    )
    
@bolt_app.action("submit")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    user = body["user"]["id"]
    temp = survey_dict[user]
    e = 20 + temp[0] - temp[5] + temp[11] - temp[15] + temp[20] - temp[25] + temp[30] - temp[35] + temp[40] - temp[45]
    a = 14 - temp[1] + temp[6] - temp[11] + temp[16] - temp[21] + temp[26] - temp[31] + temp[36] + temp[41] + temp[46]
    c = 14 + temp[2] - temp[7] + temp[12] - temp[17] + temp[22] - temp[27] + temp[32] - temp[37] + temp[42] + temp[47]
    n = 38 - temp[3] + temp[8] - temp[13] + temp[18] - temp[23] - temp[28] - temp[33] - temp[38] - temp[43] - temp[48]
    o = 8 + temp[4] - temp[9] + temp[14] - temp[19] + temp[24] - temp[29] + temp[34] + temp[39] + temp[44] + temp[49]
    text = "E %d A %d C %d N %d O %d" % (e,a,c,n,o)
    client.views_update(
               view_id=body["view"]["id"],
           # Pass a valid trigger_id within 3 seconds of receiving it
               hash=body["view"]["hash"],
           # View payload
               view={
                   "type": "modal",
               # View identifier
                   "callback_id": "view_1",
                   "title": {"type": "plain_text", "text": "Results"},
                   
                   "blocks": [
                       {
                           "type": "section",
                           "text": {"type": "mrkdwn", "text": "E %d A %d C %d N %d O %d" % (e,a,c,n,o)}
                           
                       }
                       
                       
                   ]
               }
       )
    

# Psych Survey crap
        
@bolt_app.action("psych_q1_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q2_payload
    )

@bolt_app.action("psych_q2_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q3_payload
    )

@bolt_app.action("psych_q3_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q4_payload
    )

@bolt_app.action("psych_q4_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q5_payload
    )

@bolt_app.action("psych_q5_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q6_payload
    )

@bolt_app.action("psych_q6_next")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    client.views_update(
            view_id=body["view"]["id"],
        # Pass a valid trigger_id within 3 seconds of receiving it
            hash=body["view"]["hash"],
        # View payload
            view=psych_q7_payload
    )

@bolt_app.action("psych_submit")
def action_button_click(ack, body, client):
    # Acknowledge the action
    ack();
    user = body["user"]["id"]


###############################################################################
# Event Handler
###############################################################################
@bolt_app.event("view_closed")
def action_button_click(ack, event, say):
    # Acknowledge the action
    user = event["user"]["id"]
    temp = survey_dict[user]
    e = 20 + temp[0] - temp[5] + temp[11] - temp[15] + temp[20] - temp[25] + temp[30] - temp[35] + temp[40] - temp[45]
    a = 14 - temp[1] + temp[6] - temp[11] + temp[16] - temp[21] + temp[26] - temp[31] + temp[36] + temp[41] + temp[46]
    c = 14 + temp[2] - temp[7] + temp[12] - temp[17] + temp[22] - temp[27] + temp[32] - temp[37] + temp[42] + temp[47]
    n = 38 - temp[3] + temp[8] - temp[13] + temp[18] - temp[23] - temp[28] - temp[33] - temp[38] - temp[43] - temp[48]
    o = 8 + temp[4] - temp[9] + temp[14] - temp[19] + temp[24] - temp[29] + temp[34] + temp[39] + temp[44] + temp[49]
    say("E %d A %d C %d N %d O %d" % (e,a,c,n,o))
    ack()



# Example reaction emoji echo
@bolt_app.event("reaction_added")
def reaction_added(ack, event, say, client):
    ack()
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    user = event["user"]
    ts = event["item"]["ts"]

    client.chat_postEphemeral(
        channel = channel,
        user = user,
        text = "Thank you for taking the survey! Do you think the surveys is asked too frequently or just right?",
        attachments =
            [
                {
                    "text": "Please Select an Option",
                    "fallback": "Error",
                    "callback_id": "feedback_button",
                    "color": "#3AA3E3",
                    "actions": [
                        {
                            "name": "Perfect",
                            "text": "Perfect!",
                            "type": "button",
                            "value": "Perfect"
                        },
                        {
                            "name": "Bad",
                            "text": "Too Frequent",
                            "style": "danger",
                            "type": "button",
                            "value": "Bad"
                        }
                    ]
                }
            ]
    )

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

# Psych Survey slash command (temp)
@bolt_app.command('/psych_survey')
def psych_survey(ack, body, client):
    ack();
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
            trigger_id=body["trigger_id"],
        # View payload
            view=psych_q1_payload
    )

@bolt_app.command('/startbrainstorming')
def psych_survey(ack, body, say, command, client):
    ack();
    global brainstormOn

    #Set the global listening bit to 1 to open up the container
    brainstormOn = 1
    say('Brainstorm listening has begun! A 30 minute timer has started or you can manually end the listening by using: /EndBrainstorming. Remember do not critique ideas until after the session is over')
    
    channel = command["channel_id"]
    ts = time.time()
    
    #Schedule Reminders to the group throughout the process
    client.chat_scheduleMessage(
        channel = channel,
        text = "Reminder: Brainstorm listening ends in 15 minutes. Think outside the box and dont be afraid to come up with unique ideas!",
        post_at = ts + 900,
    )

    client.chat_scheduleMessage(
        channel = channel,
        text = "Brainstorm listening has ended",
        attachments =
            [
                {
                    "text": "Please hit this Button to End Brainstorming",
                    "fallback": "Error",
                    "callback_id": "EndBrainstorming",
                    "color": "#3AA3E3",
                    "actions": [
                        {
                            "name": "EndBrainstorming",
                            "text": "End Brainstorming",
                            "type": "button",
                            "value": "End"
                        }
                    ]
                }
            ],
        post_at = ts + 1800,
    )

    client.chat_scheduleMessage(
        channel = channel,
        text = "Reminder: Look back on the Brainstorming session you had last week, was an Idea decided upon? Perhaps more mockups or another brainstorming session is needed?",
        post_at = ts + 604800,
    )

@bolt_app.command('/endbrainstorming')
def psych_survey(ack, body, say, command, client):
    ack();
    global brainstormOn

    #If brainstorming is off no need to run through the rest of the proceedures
    if (brainstormOn == 1):
        brainstormOn = 0
        say('Brainstorm listening has ended')
        channel = command["channel_id"]
        
        #Try checking if any of the scheduled messages still need to be run, if they do just delete them
        ts = time.time()
        scheduledList = client.chat_scheduledMessages_list(channel = channel, latest = ts + 1800, oldest = ts)
        for i in scheduledList['scheduled_messages']:
            try:
                client.chat_deleteScheduledMessage(channel = channel, scheduled_message_id = i["id"])
            except:
                pass

        #Iterate back to the group all of the ideas they came up with
        say('Here are all of the ideas the group came up with: ')
        item_list = list(brainDB.read_all_items())
        msg = ""
        for i in item_list:
            msg += "• " + i.get("message") + "\n"
            brainDB.delete_item(item = i.get("id"), partition_key = i.get("user"))
        say(msg)
        say("Need a mockup of one of the ideas? Try using <https://www.sketchup.com/plans-and-pricing/sketchup-free|Google Sketch up> or <https://www.figma.com/|Figma>")
        say("Also a reminder has been set for next week to look back on the brainstorming process")
    else:
        say("Brainstorming has already ended")
    


###############################################################################

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 3000)))
