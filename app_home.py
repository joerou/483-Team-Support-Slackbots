from azure.cosmos import exceptions, CosmosClient, PartitionKey

opening = """Welcome to the Amy Bot! I am here to help your team development and psychological saftey.
            On this page you can customize certain funcitonalities to best suit your teams needs as well as
            check out some interesting statistics from your channel that could help you identify certain things
            and allow your team to be more efficient in their work. Also, check out the about tab to see what 
            slash commands are available to you!\n\n\n"""

stats = list(statDB.read_all_items())
totalMessages = stats.get("total_workspace_messages")

StatsText = "*Statistics* \nBelow are some statistics from your group channel that you may be interested in!\n Total Messages Sent: %d" %(totalMessages)

app_home = {
           "type":"home",
           "blocks":[
              {
                 "type":"section",
                 "text":{
                    "type":"mrkdwn",
                    "text": opening
                 }
              },
              {
                #Horizontal divider line 
                "type": "divider"
              },
              {
                  #Section with text and a button
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Brainstorming* \nWould you like to be reminded to revisit your brainstorming session a week after?"
                  },
                  "accessory": {
                        "type": "radio_buttons",
                        "action_id": "Brainstorm_Options",
                
                        "options": [
                        {
                            "value": "1",
                            "text": {
                            "type": "plain_text",
                            "text": "Yes"
                            }   
                        },
                        {
                            "value": "0",
                            "text": {
                            "type": "plain_text",
                            "text": "No"
                            }
                        }]
                    }
                },
                #Horizontal divider line 
                {
                  "type": "divider"
                },
              {
                  #Section with text and a button
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Weekly Survey* \nHow often would you like a psychological saftey check in?"
                  },
                  "accessory": {
                        "type": "radio_buttons",
                        "action_id": "Weekly_Survey",
                
                        "options": [
                        {
                            "value": "1",
                            "text": {
                            "type": "plain_text",
                            "text": "Once a week"
                            }   
                        },
                        {
                            "value": "2",
                            "text": {
                            "type": "plain_text",
                            "text": "Once every 2 weeks"
                            }
                        },
                        {
                            "value": "3",
                            "text": {
                            "type": "plain_text",
                            "text": "Once every 3 weeks"
                            }
                        }]
                    }
                },
                #Horizontal divider line 
                {
                  "type": "divider"
                },
              {
                  #Section with text and a button
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": StatsText
                  }
                  
                }
           ]
        }