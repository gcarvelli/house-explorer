# https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from Engine.Models import *

global gameData
global aliases
global keywords
gameDate = None
aliases = None
keywords = {}

#################################
# XML Loading
#################################
"""
Loads in the game's configuration.
"""
def loadGameDataFile(file):
    tree = ET.parse(file)
    global gameData
    gameData = tree.getroot()
    
loadGameDataFile("gamedata.xml")
    
"""
Loads in the program's aliases (keywords).
"""
def loadAliasFile(file):
    tree = ET.parse(file)
    global aliases
    aliases = tree.getroot()
    
loadAliasFile("aliases.xml")

#################################
# Map
#################################

"""
Returns the name of the program, as defined in the gamedata file.
"""
def getProgramName():
    return gameData[0].text

"""
Returns the version of the program, as defined in the gamedata file.
"""
def getProgramVersion():
    return gameData[1].text

"""
Returns a constructed Player object
"""
def getPlayer():
    player = Player()
    playerNode = gameData.find("Player")
    player.name = playerNode.find("Name").text
    player.items = getItems(playerNode.find("Inventory"))
    return player

"""
Returns a dictionary of each room's id mapped to its object
"""
def getRooms():
    roomDict = {}
    for room in gameData.find("Rooms"):
        id = room.attrib["id"]
        name = room.find("Name").text
        description = room.find("Description").text.strip()
        moves = getMoves(room)
        items = getItems(room)
        aliases = getAliases(room)
        
        roomDict[id] = Room(id, name, description, moves, items, aliases)
    
    return roomDict

"""
Returns a dictionary of each Move's keyword mapped to its destination's id
"""
def getMoves(node):
    moves = {}
    for move in node.findall("Move"):
        command = move.attrib["command"].lower()
        moves[command] = move.attrib["destination"]
        
        # the moves need to be added to the keywords dictionary
        if(not command in keywords):
            keywords[command] = "move"

    return moves

"""
Returns a dictionary of each Item's name mapped to its object
"""
def getItems(node):
    items = {}
    for itemNode in node.findall("Item"):
        item = Item()
        item.name = itemNode.attrib["name"]
        item.description = itemNode.find("Description").text
        item.canPickup = itemNode.attrib["canPickup"].lower() == "true" # hacky but works
        # onPickupFail and is optional. If they aren't specified a generic message will be displayed.
        if(itemNode.find("OnPickupFail") != None):
            item.onPickupFail = itemNode.find("OnPickupFail").text
        if(itemNode.find("RoomDescriptionAddition") != None):
            item.roomDescriptionAddition = itemNode.find("RoomDescriptionAddition").text
        item.actions = []
        for actionNode in itemNode.findall("Action"):
            action = Action()
            action.performer = actionNode.attrib["performer"]
            action.onSuccess = ""
            if(actionNode.find("OnSuccess") != None):
                action.onSuccess = actionNode.find("OnSuccess").text.strip()
            action.descriptionChange = ""
            if(actionNode.find("DescriptionChange") != None):
                action.descriptionChange = actionNode.find("DescriptionChange").text.strip()
            action.itemsToAdd = []
            if(actionNode.find("AddItem") != None):
                action.itemsToAdd = getItems(actionNode.find("AddItem"))
            action.itemsToRemove = []
            for itemToRemove in actionNode.findall("RemoveItem"):
                action.itemsToRemove.append(itemToRemove.attrib["name"])
            item.actions.append(action)
                
        items[item.name] = item
    return items

"""
Returns a dictionary of each alias mapped to its command.
"""
def getAliases(node):
    aliases = {}
    for aliasNode in node.findall("Alias"):
        aliases[aliasNode.attrib["keyword"]] = aliasNode.text
    return aliases

"""
Returns the starting room.
"""
def getStartingRoom():
    roomDict = {}
    for room in gameData.find("Rooms"):        
        if("startRoom" in room.attrib.keys() and room.attrib["startRoom"].lower() == "true"):
            return room.attrib["id"]

#################################
# Keywords
#################################

keywords = {}

"""
Returns a dict of each predicate mapped to its keyword.
"""
def loadKeywords():
    global keywords
    for alias in aliases.findall("Alias"):
        keyword = alias.attrib["keyword"]
        lst = alias.text.split(',')
        for predicate in lst:
            keywords[predicate] = keyword

loadKeywords()

"""
Returns the predicate of the action.
"""
def getPredicate(action):
    # build a list of candidates and pick the longest one
    candidates = []
    for candidate in keywords:
        if(action.startswith(candidate)):
            candidates.append(candidate)
    
    longestCandidate = ""
    for candidate in candidates:
        if(len(candidate) > len(longestCandidate)):
            longestCandidate = candidate
    
    return longestCandidate

"""
Returns the keyword that the action's actual predicate was mapped to.
"""
def getKeyword(action):
    if(getPredicate(action) in keywords):
        return keywords[getPredicate(action)]
    else:
        return ""

"""
Returns the action with the predicate removed.
"""
def removePredicate(action):
    predicate = getPredicate(action)
    return action[len(predicate):].strip()


