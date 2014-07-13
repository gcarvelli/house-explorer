# https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from Engine.Models import Item, Room

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
Returns a dictionary of each room's id mapped to its object
"""
def getRooms():
    roomDict = {}
    for room in root.find("Rooms"):
        id = room.attrib["id"]
        name = room.find("Name").text
        description = room.find("Description").text
        moves = {}
        for move in root.findall("Move"):
            moves[move.attrib["command"]] = move.attrib["destination"]
        items = []
        for item in root.findall("Item"):
            items.append(Item(item.attrib["name"], item.find("Description").text.strip("\n \t"), item.attrib["canPickup"].lower() == "true")) # hacky
        
        roomDict[id] = Room(id, name, description, moves, items)
    return roomDict

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