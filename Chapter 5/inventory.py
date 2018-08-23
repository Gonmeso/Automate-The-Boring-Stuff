# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 08:06:55 2018

@author: Gonzalo Mellizo
"""
#Fantasy Game Inventory Practice Project

mainInventory = { 'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        totalItems += value
        
    print('Total number of items: ' + str(totalItems))
    
displayInventory(mainInventory)

