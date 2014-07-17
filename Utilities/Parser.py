# https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from Engine.Models import Player, Item, Room

global tree
global root
tree = ET.parse("gamedata.xml")
root = tree.getroot()

def loadFile(file):
    tree = ET.parse(file)
    root = tree.getroot()

"""
Returns the name of the program, as defined in the gamedata file.
"""
def getProgramName():
    return root[0].text

"""
Returns the version of the program, as defined in the gamedata file.
"""
def getProgramVersion():
    return root[1].text

"""
Returns a constructed Player object
"""
def getPlayer():
    player = Player()
    playerNode = root.find("Player")
    player.name = playerNode.find("Name").text
    player.items = getItems(playerNode.find("Inventory"))
    return player

"""
Returns a dictionary of each room's id mapped to its object
"""
def getRooms():
    roomDict = {}
    for room in root.find("Rooms"):
        id = room.attrib["id"]
        name = room.find("Name").text
        description = room.find("Description").text.strip()
        moves = getMoves(room)
        items = getItems(room)
        
        roomDict[id] = Room(id, name, description, moves, items)
    
    return roomDict

"""
Returns a dictionary of each Move's keyword mapped to its destination's id
"""
def getMoves(node):
    moves = {}
    for move in node.findall("Move"):
        moves[move.attrib["command"].lower()] = move.attrib["destination"]
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
        # onPickupFail is optional. If it isn't specified a generic message will be displayed.
        if(itemNode.find("OnPickupFail") != None):
            item.onPickupFail = itemNode.find("OnPickupFail").text
        items[item.name] = item
    return items

"""
Returns the starting room.
"""
def getStartingRoom():
    roomDict = {}
    for room in root.find("Rooms"):        
        if("startRoom" in room.attrib.keys() and room.attrib["startRoom"].lower() == "true"):
            return room.attrib["id"]

"""
Returns a string of each room's name and description. For debugging use only.
"""
def getRoomsString():
    # find the rooms tag
    rooms = root.find("Rooms")
    s = ""
    for room in rooms:
        s += room.find("Name").text + "\n"
    return s