# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:06:56 2018

@author: Gonzalo Mellizo-Soto
"""

import re, glob

print('Please, supply a regular expression: ')
regex = input()
reToFind = re.compile(regex)

textFiles = glob.glob('*.txt')

for file in textFiles:
    currentFile = open(file, 'r')
    textLines = currentFile.readlines()
    for line in textLines:
        result = reToFind.search(line)
        if result is not None:
            print(line)
    currentFile.close()