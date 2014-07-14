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
        action = input().strip(' ')
        if(action.lower() == "look"): 
            lookAround()
        elif(action.lower() in currentRoom.moves):
            currentRoom = roomDict[currentRoom.moves[action]]
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