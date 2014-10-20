import sys
import os
from Utilities import Parser
from Engine.Run import runEngine

# Do a python version check (greater than 3.0.0)
if(sys.hexversion < 0x03000000):
	print("House Explorer requires Python 3.0 or greater.")
	sys.exit(1)

sys.path.append(os.getcwd())

if(__name__ == "__main__"):
    
    # if the user specified a gamedata file, load it up
    if(len(sys.argv) > 1):
        Parser.loadGameDataFile(sys.argv[1])
    else:
        Parser.loadGameDataFile("gamedata.xml")
        
    # start game loop
    runEngine()
