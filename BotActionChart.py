#all this does is stores a data structure that is used to check the users input and depending on that the bot will perform specific actions
#this is essentially the scripted portion of the chatbot
#for example when the chatbot asks the user if they want depression resources and the user says yes,
#the chatbot will come to this data structure find keyword depression, then do the action associated with depression and confirmation
actionChart = {
  "depression": {"confirmation": "Here are some Links to resources for depression: ________", "decline": "Ok, but I'll be here if you change your mind."},
  "stress": {"confirmation": "Here are some Links to resources for stress: ________", "decline": "Ok, but you should really think about taking things easier." },
  "loneliness": {"confirmation": "Here are some Links to resources for loneliness: ________", "decline": "Ok, if you want to talk I'll always be here." },
}