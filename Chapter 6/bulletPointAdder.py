# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 17:27:34 2018

@author: Gonzalo Mellizo
"""

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text in the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add the star
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)