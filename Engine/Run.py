import os
from Engine.Models import *
from Utilities.TextControl import wrap
from Utilities import Parser

def runEngine():
    # get the map
    roomDict = Parser.getRooms()
    global currentRoom
    currentRoom = roomDict[Parser.getStartingRoom()]
    
    # get the player
    global player
    player = Parser.getPlayer()
    
    lookAround()
    
    while(True):
        action = input().strip(' ').split(' ')
        
        if(len(action) == 0):
            continue
        
        if(action[0].lower() == "look"): 
            if(len(action) > 1 and action[1].lower() == "at"):
                if(len(action) == 2):
                    wrap("Look at what?")
                else:
                    item = " ".join(action[2:])
                    if(item in currentRoom.items):
                        wrap(currentRoom.items[item].description)
                    elif(item in player.items):
                        wrap(player.items[item].description)
                    else:
                        wrap("There isn't one of those around right now.")
            else:
                lookAround()
        elif(action[0] == "pick"):
            if(len(action) > 1 and action[1].lower() == "up"):
                if(len(action) == 2):
                    wrap("Pick up what?")
                else:
                    item = " ".join(action[2:])
                    if(item in currentRoom.items):
                        if(currentRoom.items[item].canPickup):
                            player.items[item] = currentRoom.items[item]
                            del currentRoom.items[item]
                            wrap(item + " added.")
                        else:
                            if(currentRoom.items[item].onPickupFail != ""):
                                wrap(currentRoom.items[item].onPickupFail)
                            else:
                                wrap("That cannot be picked up.")
                    else:
                        wrap("There isn't one of those around right now.")
        elif(action[0].lower() == "inventory"):
            if(len(player.items) == 0):
                wrap("You have nothing in your inventory.")
            else:
                wrap("In your inventory you have:")
                for item in player.items:
                    wrap("    " + item)
        elif(action[0].lower() in currentRoom.moves):
            currentRoom = roomDict[currentRoom.moves[action[0]]]
            lookAround()
        else:
            print("Command not recognized")

def lookAround():
    clear()
    print('\n')
    wrap(currentRoom.name)
    wrap(currentRoom.description)
    print('\n')
    
    
def clear():
    os.system('cls')
    wrap(Parser.getProgramName())
    wrap('Version ' + Parser.getProgramVersion())