
class Room():
    
    __slots__ = ('id', 'name','description', 'moves', 'items')

    def __init__(self, id="", name="", description="", moves={}, items={}):
        self.id = id
        self.name = name
        self.description = description
        self.moves = moves
        self.items = items
        
class Item():
    
    __slots__ = ('name', 'description', 'canPickup', 'onPickupFail')
    
    def __init__(self, name="", description="", canPickup=False, onPickupFail=""):
        self.name = name
        self.description = description
        self.canPickup = canPickup
        self.onPickupFail = onPickupFail

class Player():
    __slots__=('name','items')
    
    def __init__(self, name="", items = {}):
        self.name=name
        self.items = {}
