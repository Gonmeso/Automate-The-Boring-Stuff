# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 08:13:53 2018

@author: Gonzalo Mellizo
"""
# List to dictionary funtion for fantasy game practice project

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger','gold coin','gold coin','ruby']

inv = addToInventory(inv, dragonLoot)
#displayInventory(inv)