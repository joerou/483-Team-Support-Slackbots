question1_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 1"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am the life of the party"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "button_abc"
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