
class Room():
    
    __slots__ = ('id', 'name','description', 'moves', 'items', 'aliases')

    def __init__(self, id="", name="", description="", moves={}, items={}, aliases={}):
        self.id = id
        self.name = name
        self.description = description
        self.moves = moves
        self.items = items
        self.aliases = aliases
    
    def getDescription(self):
        ret = self.description
        for itemName in self.items:
            if(self.items[itemName].roomDescriptionAddition != ""):
                ret += " " + self.items[itemName].roomDescriptionAddition
        return ret
        
class Item():
    
    __slots__ = ('name', 'description', 'canPickup', 'onPickupFail', 'roomDescriptionAddition', 'actions', 'aliases')
    
    def __init__(self, name="", description="", canPickup=False, onPickupFail="", roomDescriptionAddition="", actions=[]):
        self.name = name
        self.description = description
        self.canPickup = canPickup
        self.onPickupFail = onPickupFail
        self.roomDescriptionAddition = roomDescriptionAddition
        self.actions = actions

class Player():
    __slots__ = ('name','items')
    
    def __init__(self, name="", items = {}):
        self.name = name
        self.items = items

class Action():
    
    __slots__ = ('performer', 'onSuccess', 'descriptionChange', 'itemsToAdd', 'itemsToRemove')

    def __init__(self, performer="", onSuccess="", descriptionChange="", itemsToAdd=[], itemsToRemove=[]):
        self.performer = performer
        self.onSuccess = onSuccess
        self.descriptionChange = descriptionChange
        self.itemsToAdd = itemsToAdd
        self.itemsToRemove = itemsToRemove

    

        