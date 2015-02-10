from Utilities.TextControl import wrap
import os

class Room():
    
    __slots__ = ('id', 'name','description', 'moves', 'items', 'aliases', 'actions')

    def __init__(self, id="", name="", description="", moves={}, items={}, aliases={}, actions={}):
        self.id = id
        self.name = name
        self.description = description
        self.moves = moves
        self.items = items
        self.aliases = aliases
        self.actions = actions
    
    def getDescription(self):
        ret = self.description
        ret += os.linesep
        for itemName in self.items:
            if(self.items[itemName].roomDescriptionAddition != ""):
                ret += os.linesep + self.items[itemName].roomDescriptionAddition
        return ret
        
class Item():
    
    __slots__ = ('name', 'description', 'canPickup', 'onPickupFail', 'roomDescriptionAddition', 'aliases')
    
    def __init__(self, name="", description="", canPickup=False, onPickupFail="", roomDescriptionAddition=""):
        self.name = name
        self.description = description
        self.canPickup = canPickup
        self.onPickupFail = onPickupFail
        self.roomDescriptionAddition = roomDescriptionAddition

class Player():
    __slots__ = ('name','items')
    
    def __init__(self, name="", items = {}):
        self.name = name
        self.items = items

class Action():
    
    __slots__ = ('performer', 'reciever', 'onSuccess', 'descriptionChange', 'itemsToAdd', 'itemsToRemove', 'itemsToAddToRooms')

    def __init__(self, performer="", reciever="", onSuccess="", descriptionChange="", itemsToAdd=[], itemsToRemove=[], itemsToAddToRooms={}):
        self.performer = performer
        self.reciever = reciever
        self.onSuccess = onSuccess
        self.descriptionChange = descriptionChange
        self.itemsToAdd = itemsToAdd
        self.itemsToRemove = itemsToRemove
        self.itemsToAddToRooms = itemsToAddToRooms

    def execute(self, player, currentRoom, rooms):
        # print success message
        wrap(self.onSuccess)
        # change description
        currentRoom.items[self.reciever].description = self.descriptionChange
        # add items
        for itemToAdd in self.itemsToAdd:
            player.items[itemToAdd] = self.itemsToAdd[itemToAdd]
        # remove items
        for itemToRemove in self.itemsToRemove:
            del player.items[itemToRemove]

        # add items to rooms
        for room, itemList in self.itemsToAddToRooms.items():
            # merge the rooms[room].items and itemList dicts
            rooms[room].items = dict(list(rooms[room].items.items()) + list(itemList.items()))    

        