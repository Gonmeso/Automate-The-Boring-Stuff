#!python3
# strip.py - regex version of strip()

import re

exampleText = ['hi', '  hihi ', ' bye', 'good', ' b a d ']

def regexStrip(text, charToStrip = None):
    if charToStrip == None:
        stripReg = re.compile(r'(^ *)|( *$)')
        print(stripReg.sub('', text))
    else:
        stripReg = re.compile('[{}]'.format(str(charToStrip)))
        print(stripReg.sub('', text))

for word in exampleText:
    regexStrip(word)
