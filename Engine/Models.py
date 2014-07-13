
class Room():
    
    __slots__ = ('id', 'name','description', 'moves', 'items')

    def __init__(self, id, name, description, moves, items):
        self.id = id
        self.name = name
        self.description = description
        self.moves = moves
        self.items = items
        
class Item():
    
    __slots__ = ('name', 'description', 'canPickup')
    
    def __init__(self, name, description, canPickup):
        self.name = name
        self.description = description
        self.canPickup = canPickup

