'''
Created on Jul 12, 2014

@author: Giovanni
'''
import unittest
import sys
import os
from Utilities import Parser


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetProgramName(self):
        self.assertEqual(Parser.getProgramName(), "House Explorer")
        
    def testGetProgramVersion(self):
        self.assertEqual(Parser.getProgramVersion(), "1.0")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    sys.path.append(os.getcwd())
    print(os.getcwd())
    Parser.loadFile("testparser.xml")
    unittest.main()

def runTests():
    print(Parser.getProgramName())
    print(Parser.getProgramVersion())
    print(Parser.getRoomsString())
    os.system("cls")
    roomDict = Parser.getRooms()
    for id in roomDict:
        print("\n" + roomDict[id].name)
        print(roomDict[id].description)
