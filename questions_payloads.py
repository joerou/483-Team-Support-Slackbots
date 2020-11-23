
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
                "action_id": "question1_next"
            }
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": ""},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Back"},
                "action_id": "question1_back"
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


question2_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 2"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I feel little concern for others"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question2_next"
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
                "value": "Q2_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q2_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q2_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q2_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q2_5",
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



question3_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 3"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am always prepared"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question3_next"
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
                "value": "Q3_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q3_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q3_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q3_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q3_5",
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


question4_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 4"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I get stressed out easily"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question4_next"
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
                "value": "Q4_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q4_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q4_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q4_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q4_5",
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


question5_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 5"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have a rich vocabulary"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question5_next"
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
                "value": "Q5_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q5_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q5_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q5_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q5_5",
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


question6_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 6"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I don't talk a lot"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question6_next"
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
                "value": "Q6_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q6_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q6_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q6_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q6_5",
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


question7_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am interested in people"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question7_next"
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
                "value": "Q7_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q7_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q7_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q7_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q7_5",
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


question8_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 8"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I leave my belongings around"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question8_next"
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
                "value": "Q8_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q8_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q8_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q8_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q8_5",
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


question9_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 9"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am relaxed most of the time"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question9_next"
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
                "value": "Q9_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q9_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q9_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q9_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q9_5",
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


question10_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 10"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have difficulty understanding abstract ideas"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question10_next"
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
                "value": "Q10_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q10_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q10_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q10_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q10_5",
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


question11_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 11"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I feel comfortable around people"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question11_next"
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
                "value": "Q11_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q11_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q11_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q11_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q11_5",
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


question12_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 12"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I insult people"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question12_next"
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
                "value": "Q12_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q12_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q12_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q12_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q12_5",
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


question13_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 13"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I pay attention to details"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question13_next"
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
                "value": "Q13_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q13_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q13_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q13_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q13_5",
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


question14_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 14"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I worry about things"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question14_next"
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
                "value": "Q14_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q14_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q14_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q14_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q14_5",
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


question15_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 15"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have a vivid imagination"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question15_next"
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
                "value": "Q15_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q15_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q15_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q15_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q15_5",
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

question16_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 16"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I keep in the background"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question16_next"
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
                "value": "Q16_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q16_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q16_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q16_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q16_5",
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


question17_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 17"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I sympothize with other's feelings"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question17_next"
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
                "value": "Q17_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q17_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q17_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q17_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q17_5",
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


question18_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 18"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I make a mess of things"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question18_next"
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
                "value": "Q18_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q18_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q18_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q18_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q18_5",
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


question19_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 19"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I seldom feel blue"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question19_next"
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
                "value": "Q19_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q19_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q19_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q19_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q19_5",
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


question20_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 20"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am not interested in abstract ideas"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question20_next"
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
                "value": "Q20_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q20_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q20_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q20_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q20_5",
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


question21_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 21"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I start conversations"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question21_next"
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
                "value": "Q21_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q21_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q21_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q21_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q21_5",
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


question22_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 22"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am not interested in other people's problems"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question22_next"
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
                "value": "Q22_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q22_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q22_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q22_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q22_5",
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


question23_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 23"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I get chores done right away"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question23_next"
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
                "value": "Q23_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q23_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q23_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q23_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q23_5",
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


question24_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 24"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am easily disturbed"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question24_next"
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
                "value": "Q24_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q24_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q24_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q24_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q24_5",
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


question25_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 25"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have excellent ideas"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question25_next"
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
                "value": "Q25_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q25_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q25_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q25_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q25_5",
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


question26_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 26"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have little to say"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question26_next"
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
                "value": "Q26_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q26_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q26_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q26_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q26_5",
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


question27_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 27"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have a soft heart"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question27_next"
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
                "value": "Q27_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q27_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q27_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q27_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q27_5",
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


question28_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 28"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I often forget to put things in their proper places"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question28_next"
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
                "value": "Q28_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q28_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q28_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q28_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q28_5",
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


question29_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 29"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I get upset easily"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question29_next"
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
                "value": "Q29_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q29_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q29_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q29_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q29_5",
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


question30_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 30"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I do not have a good imagination"},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question30_next"
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
                "value": "Q30_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q30_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q30_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q30_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q30_5",
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


question31_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 31"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I talk to a lot of different people at parties"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question31_next"
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
                "value": "Q31_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q31_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q31_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q31_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q31_5",
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


question32_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 32"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am not really interested in others"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question32_next"
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
                "value": "Q32_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q32_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q32_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q32_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q32_5",
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


question33_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 33"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am not really interested in others"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question33_next"
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
                "value": "Q33_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q33_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q33_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q33_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q33_5",
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


question34_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 34"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I change my mood a lot"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question34_next"
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
                "value": "Q34_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q34_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q34_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q34_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q34_5",
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


question35_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 35"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am quick to understand things"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question35_next"
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
                "value": "Q35_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q35_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q35_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q35_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q35_5",
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


question36_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 36"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I don't like to draw attention to myself"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question36_next"
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
                "value": "Q36_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q36_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q36_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q36_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q36_5",
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


question37_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 37"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I take time out for others"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question37_next"
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
                "value": "Q37_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q37_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q37_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q37_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q37_5",
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


question38_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 38"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I take time out for others"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question38_next"
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
                "value": "Q38_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q38_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q38_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q38_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q38_5",
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


question39_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 39"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I have frequent mood swings"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question39_next"
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
                "value": "Q39_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q39_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q39_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q39_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q39_5",
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


question40_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 40"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I use difficult words"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question40_next"
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
                "value": "Q40_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q40_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q40_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q40_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q40_5",
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


question41_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 41"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I don't mind being the center of attention"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question41_next"
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
                "value": "Q41_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q41_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q41_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q41_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q41_5",
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


question42_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 42"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I feel others' emotions"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question42_next"
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
                "value": "Q42_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q42_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q42_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q42_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q42_5",
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


question43_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 43"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I follow a schedule"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question43_next"
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
                "value": "Q43_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q43_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q43_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q43_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q43_5",
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


question44_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 44"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I get irritated easily"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question44_next"
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
                "value": "Q44_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q44_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q44_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q44_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q44_5",
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
        
        
    



question45_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 45"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I spend time reflecting on things"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question45_next"
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
                "value": "Q45_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q45_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q45_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q45_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q45_5",
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


question46_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 46"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am quiet around strangers"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question46_next"
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
                "value": "Q46_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q46_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q46_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q46_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q46_5",
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


question47_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 47"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I make people feel at ease"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question47_next"
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
                "value": "Q47_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q47_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q47_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q47_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q47_5",
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


question48_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 48"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am exacting in my work"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question48_next"
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
                "value": "Q48_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q48_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q48_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q48_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q48_5",
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


question49_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 49"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I often feel blue"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "question49_next"
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
                "value": "Q49_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q49_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q49_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q49_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q49_5",
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


question50_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 50"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "I am full of ideas"},
            "accessory":{
                "type": "button",
                "text": {"type": "plain_text", "text": "Submit"},
                "action_id": "submit"
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
                "value": "Q50_1",
                "text": {
                  "type": "plain_text",
                  "text": "1 Strongly Disagree"
                }
              },
              {
                "value": "Q50_2",
                "text": {
                  "type": "plain_text",
                  "text": "2"
                }
              },
              {
                "value": "Q50_3",
                "text": {
                  "type": "plain_text",
                  "text": "3"
                }
              },
              {
                "value": "Q50_4",
                "text": {
                  "type": "plain_text",
                  "text": "4"
                }
              },
              {
                "value": "Q50_5",
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


# Payload for psych survey
psych_q1_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 1/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "1. If you make a mistake on this team, it is often held against you."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q1_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q1_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q1_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q1_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q1_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q1_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q2_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 2/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "2. Members of this team are able to bring up problems and tough issues."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q2_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q2_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q2_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q2_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q2_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q2_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q3_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 3/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "3. People on this team sometimes reject others for being different."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q3_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q3_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q3_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q3_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q3_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q3_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q4_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 4/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "4. It is safe to take a risk on this team."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q4_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q4_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q4_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q4_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q4_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q4_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q5_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 5/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "5. It is difficult to ask other members of this team for help."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q5_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q5_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q5_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q5_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q5_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q5_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q6_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 6/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "6. No one on this team would deliberately act in a way that undermines my efforts."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Next"},
                "action_id": "psych_q6_next"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q6_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q6_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q6_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q6_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q6_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}

psych_q7_payload = {
    "type": "modal",
# View identifier
    "callback_id": "view_1",
    "title": {"type": "plain_text", "text": "Question 7/7"},
    
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "7. Working with members of this team, my unique skills and talents are valued and utilized."},
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": "Submit"},
                "action_id": "psych_submit"
            }
        },
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Select the option that best represents your opinion."
          },
          "accessory": {
            "type": "radio_buttons",
            "action_id": "psych_radio_id",
            
            "options": [
              {
                "value": "psych_q7_1",
                "text": {
                  "type": "plain_text",
                  "text": "very inaccurate"
                }
              },
              {
                "value": "psych_q7_2",
                "text": {
                  "type": "plain_text",
                  "text": "inaccurate"
                }
              },
              {
                "value": "psych_q7_3",
                "text": {
                  "type": "plain_text",
                  "text": "neutral"
                }
              },
              {
                "value": "psych_q7_4",
                "text": {
                  "type": "plain_text",
                  "text": "accurate"
                }
              },
              {
                "value": "psych_q7_5",
                "text": {
                  "type": "plain_text",
                  "text": "very accurate"
                }
              }
            ]
          }
        }
        
        
    ]
}
