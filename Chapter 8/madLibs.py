# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 19:36:06 2018

@author: Gonzalo Mellizo-Soto
"""
import re

text = open('testText.txt', 'r')
shortText = text.read()
shortText = shortText.split(' ')
text.close()


for idx,word in enumerate(shortText):
    if 'ADJECTIVE' in word:
        print('Entry an adjective:')
        newWord = input()
        shortText[idx] = newWord
    elif 'NOUN' in word: 
        print('Entry a noun:')
        newWord = input()
        shortText[idx] = newWord
    elif 'ADVERB' in word: 
        print('Entry an adverb:')
        newWord = input()
        shortText[idx] = newWord
    elif 'VERB' in word:
        print('Entry a verb:')
        newWord = input()
        shortText[idx] = newWord
        
shortText = ' '.join(shortText)
print(shortText)

newFile = open('Newtext.txt', 'w')
newFile.write(shortText)
newFile.close()