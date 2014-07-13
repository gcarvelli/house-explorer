import sys
import os
from Utilities import Parser
from Engine.Run import runEngine

sys.path.append(os.getcwd())

if(__name__ == "__main__"):
    
    # if the user specified a gamedata file, load it up
    if(len(sys.argv) > 1):
        Parser.loadFile(sys.argv[1])
    else:
        Parser.loadFile("gamedata.xml")
        
    # start game loop
    runEngine()