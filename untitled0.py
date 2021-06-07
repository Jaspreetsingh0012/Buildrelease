# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:26:13 2021

@author: hp
"""

import json
from difflib import get_close_matches

data=json.load(open("076 data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    
    elif len(get_close_matches(w,data.keys()))>0:
        yes_no=input( "Did you mean %s, Press 'Y' if yes otherwise 'N' "%get_close_matches(w,data.keys())[0])
        if yes_no == "Y" or yes_no == "y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Not a word, Please double check it"
    else:
        return "Not a word, Please double check it"

word= input("Enter the word:  ")
meaning = translate(word)
if type(meaning) == list:
    for i in meaning:
        print(i)
else:
    print(meaning)