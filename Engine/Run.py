import os
from Engine.Models import *
from Utilities.TextControl import wrap
from Utilities import Parser

def runEngine():
    # get the map
    roomDict = Parser.getRooms()
    global currentRoom
    currentRoom = roomDict[Parser.getStartingRoom()]
    
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
                    else:
                        wrap("There isn't one of those around right now.")
            else:
                lookAround()
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