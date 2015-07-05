
import xml.etree.ElementTree as ET
from Engine.Models import *
from Engine.GameData import GameData

class XMLParser:

    def parseGameData(self, gameDataFile, itemFile):
        self.gameDataFile = gameDataFile
        self.root = ET.parse(gameDataFile).getroot()

        self.itemFile = itemFile
        self.itemRoot = ET.parse(itemFile).getroot()

        gameData = GameData()

        gameData.programName = self.root[0].text

        gameData.programVersion = self.root[1].text

        gameData.player = self._getPlayer()

        gameData.rooms = self._getRooms(gameData)

        return gameData

    def _getPlayer(self):
        player = Player()
        playerNode = self.root.find("Player")
        player.name = playerNode.find("Name").text
        player.items = self._getItems(playerNode.find("Inventory"))

        return player

    def _getRooms(self, gameData):
        roomDict = {}
        for room in self.root.find("Rooms"):
            id = room.attrib["id"]
            name = room.find("Name").text
            description = room.find("Description").text.strip()
            moves = self._getMoves(room)
            items = self._getItems(room)
            aliases = self._getAliases(room)
            actions = {}

            for actionNode in room.findall("Action"):
                action = Action()
                action.performer = actionNode.attrib["performer"]
                action.reciever = actionNode.attrib["reciever"]
                action.onSuccess = ""
                if(actionNode.find("OnSuccess") != None):
                    action.onSuccess = actionNode.find("OnSuccess").text.strip()
                    
                action.descriptionChange = ""
                if(actionNode.find("DescriptionChange") != None):
                    action.descriptionChange = actionNode.find("DescriptionChange").text.strip()

                action.itemsToAdd = []
                if(actionNode.find("AddToInventory") != None):
                    action.itemsToAdd = self._getItems(actionNode.find("AddToInventory"))

                action.itemsToAddToRooms = {}
                for node in actionNode.findall("AddToRoom"):
                    # when no room is defined the default is the current room
                    roomName = node.attrib['room'] if 'room' in node.attrib else id
                    action.itemsToAddToRooms[roomName] = self._getItems(node)
                    
                action.itemsToRemove = []
                for itemToRemove in actionNode.findall("RemoveFromInventory"):
                    action.itemsToRemove.append(itemToRemove.attrib["name"])


                for keyword in actionNode.findall("Keyword"):
                    actions[keyword.text.strip()] = action

            roomDict[id] = Room(id, name, description, moves, items, aliases, actions)

            if("startRoom" in room.attrib.keys() and room.attrib["startRoom"].lower() == "true"):
                gameData.startRoom = id

        return roomDict

    def _getMoves(self, node):
        moves = {}
        for move in node.findall("Move"):
            command = move.attrib["command"].lower()
            moves[command] = move.attrib["destination"]

        return moves

    def _getItems(self, node):
        items = {}
        for itemNode in node.findall("Item"):
            if "ref_id" in itemNode.attrib:
                # the item is listed in the items file
                for itemRefNode in self.itemRoot:
                    if itemRefNode.attrib["id"] == itemNode.attrib["ref_id"]:
                        itemNode = itemRefNode
                        break

            item = Item()
            item.name = itemNode.attrib["name"]
            item.description = itemNode.find("Description").text.strip()
            item.canPickup = itemNode.attrib["canPickup"].lower() == "true"
            # onPickupFail and is optional. If they aren't specified a generic message will be displayed.
            if(itemNode.find("OnPickupFail") != None):
                item.onPickupFail = itemNode.find("OnPickupFail").text.strip()
            if(itemNode.find("RoomDescriptionAddition") != None):
                item.roomDescriptionAddition = itemNode.find("RoomDescriptionAddition").text.strip()
            if(itemNode.find("DropDescriptionAddition") != None):
                item.dropDescriptionAddition = itemNode.find("DropDescriptionAddition").text.strip()

            items[item.name] = item
        return items

    def _getAliases(self, node):
        aliases = {}
        for aliasNode in node.findall("Alias"):
            aliases[aliasNode.attrib["keyword"]] = aliasNode.text
        return aliases

    def parseAliases(self, aliasFile):
        self.aliasFile = aliasFile
        self.aliasRoot = ET.parse(aliasFile).getroot()

        return self._getAliases(self.aliasRoot)
