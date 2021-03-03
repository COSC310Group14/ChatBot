# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:08:01 2021

@author: jkran
"""

import random

bot_name = "Thera-bot"

def get_response(msg):

    # testing, we just send back random shit
    if True:
        return random.choice(responses)
    else:
        return "I do not understand..."
    
responses = ["hello", "beans", "goodbye"]
    

