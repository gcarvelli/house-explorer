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
        action = input().strip(' ')
        
        predicate = Parser.getPredicate(action)
        object = Parser.removePredicate(action)
        keyword = Parser.getKeyword(action)
        
        if(len(action) == 0):
            continue
        
        if(keyword == "look"):
            lookAround()
        elif(keyword == "look at"):
            if(object in currentRoom.items):
                wrap(currentRoom.items[object].description)
            elif(object in player.items):
                wrap(player.items[object].description)
            else:
                wrap("There isn't one of those around right now.")
        elif(keyword == "take"):
            if(object in currentRoom.items):
                if(currentRoom.items[object].canPickup):
                    player.items[object] = currentRoom.items[object]
                    del currentRoom.items[object]
                    wrap(object + " added.")
                else:
                    if(currentRoom.items[object].onPickupFail != ""):
                        wrap(currentRoom.items[object].onPickupFail)
                    else:
                        wrap("That cannot be picked up.")
            else:
                wrap("There isn't one of those around right now.")
        elif(keyword == "use"):
            if(object == ""):
                wrap("Use what on what?")
                continue
            items = object.split(" on ")
            performer = items[0]
            reciever = None
            if(len(items) > 1):
                reciever = items[1]
            if(reciever != None):
                if(performer in player.items):
                    thisAction = None
                    for candidate in currentRoom.items[reciever].actions:
                        if(candidate.performer == performer):
                            thisAction = candidate
                            break
                    if(thisAction != None):
                        # print success message
                        wrap(thisAction.onSuccess)
                        # change description
                        currentRoom.items[reciever].description = thisAction.descriptionChange
                        # add items
                        for itemToAdd in thisAction.itemsToAdd:
                            player.items[itemToAdd] = thisAction.itemsToAdd[itemToAdd]
                        # remove items
                        for itemToRemove in thisAction.itemsToRemove:
                            del player.items[itemToRemove]
                    else:
                        wrap("That's not possible.")
                else:
                    wrap("You don't have a " + items[0] + ".")
            else:
                wrap("You can't use an item by itself, yet.")
        elif(keyword == "inventory"):
            if(len(player.items) == 0):
                wrap("You have nothing in your inventory.")
            else:
                wrap("In your inventory you have:")
                for item in player.items:
                    wrap("    " + item)
        elif(keyword == "move"):
            currentRoom = roomDict[currentRoom.moves[predicate]]
            lookAround()
        else:
            print("Command not recognized.")

def lookAround():
    clear()
    print('\n')
    wrap(currentRoom.name)
    wrap(currentRoom.getDescription())
    print('\n')
    
    
def clear():
    os.system('cls')
    wrap(Parser.getProgramName())
    wrap('Version ' + Parser.getProgramVersion())