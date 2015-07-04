import sys
import os
from Utilities import Parser
from Engine.Run import runEngine

# Do a python version check (greater than 3.0.0)
if(sys.hexversion < 0x03000000):
	print("House Explorer requires Python 3.0 or greater.")
	sys.exit(1)

if(__name__ == "__main__"):

    files = {}
    files["aliases"] = ".config/aliases.xml"
    files["items"] = ".config/items.xml"

    # if the user specified a gamedata file, load it up
    if(len(sys.argv) > 1):
        files["gameData"] = sys.argv[1]
    else:
        files["gameData"] = ".config/gamedata.xml"

    Parser.parse(**files)
        
    # start game loop
    runEngine()
