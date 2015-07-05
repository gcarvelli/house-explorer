import sys
import os
from Utilities.CommandParser import CommandParser
from Utilities.XMLParser import XMLParser
from Engine.Run import runEngine

# Do a python version check (greater than 3.0.0)
if(sys.hexversion < 0x03000000):
	print("House Explorer requires Python 3.0 or greater.")
	sys.exit(1)

if(__name__ == "__main__"):

    aliasFile = ".config/aliases.xml"
    itemsFile = ".config/items.xml"
    gameDataFile = ".config/gameData.xml"

    # put together the config for the engine
    config = {}

    parser = XMLParser()

    # Aliases
    commandParser = CommandParser(parser.parseAliases(aliasFile))
    config["commandParser"] = commandParser

    # GameData / Items
    config["gameDataObj"] = parser.parseGameData(gameDataFile, itemsFile)
        
    # start game loop
    runEngine(**config)
