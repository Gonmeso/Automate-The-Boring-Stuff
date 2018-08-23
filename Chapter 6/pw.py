# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:59:18 2018

@author: solutio
"""

#! python3
# pw.py - An insecire password locker program

PASSWORDS = {'email': 'qwertyMola',
             'server': '_DOsep18_'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)