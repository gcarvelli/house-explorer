
class Room():
    
    __slots__ = ('id', 'name','description', 'moves', 'items')

    def __init__(self, id="", name="", description="", moves={}, items={}):
        self.id = id
        self.name = name
        self.description = description
        self.moves = moves
        self.items = items
    
    def getDescription(self):
        ret = self.description
        for itemName in self.items:
            if(self.items[itemName].roomDescriptionAddition != ""):
                ret += " " + self.items[itemName].roomDescriptionAddition
        return ret
        
class Item():
    
    __slots__ = ('name', 'description', 'canPickup', 'onPickupFail', 'roomDescriptionAddition')
    
    def __init__(self, name="", description="", canPickup=False, onPickupFail="", roomDescriptionAddition=""):
        self.name = name
        self.description = description
        self.canPickup = canPickup
        self.onPickupFail = onPickupFail
        self.roomDescriptionAddition = roomDescriptionAddition

class Player():
    __slots__=('name','items')
    
    def __init__(self, name="", items = {}):
        self.name=name
        self.items = {}
