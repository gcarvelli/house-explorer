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

    #################################
    # Map
    #################################

    def testGetProgramName(self):
        self.assertEqual(Parser.getProgramName(), "House Explorer")
        
    def testGetProgramVersion(self):
        self.assertEqual(Parser.getProgramVersion(), "1.0")

    #################################
    # Keywords
    #################################
    
    def testGetPredicate(self):
        self.assertEqual(Parser.getPredicate("look at bookshelf"), "look at")
        self.assertEqual(Parser.getPredicate("look bookshelf"), "look")
        self.assertEqual(Parser.getPredicate("look at"), "look at")
        self.assertEqual(Parser.getPredicate("look"), "look")
    
    def testGetKeyword(self):
        self.assertEqual(Parser.getKeyword("look around"), "look")
        self.assertEqual(Parser.getKeyword("look at bookshelf"), "look at")
        self.assertEqual(Parser.getKeyword("take basketball"), "take")
        self.assertEqual(Parser.getKeyword("pick up basketball"), "take")
        self.assertEqual(Parser.getKeyword("grab basketball"), "take")
        
        
    def testRemovePredicate(self):
        self.assertEqual(Parser.removePredicate("look around"), "")
        self.assertEqual(Parser.removePredicate("look at bookshelf"), "bookshelf")
        self.assertEqual(Parser.removePredicate("take basketball"), "basketball")
        self.assertEqual(Parser.removePredicate("pick up basketball"), "basketball")
        self.assertEqual(Parser.removePredicate("grab basketball"), "basketball")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # this path needs to be appended here because setUp is run from the base directory
    sys.path.append(os.getcwd())
    Parser.loadGameDataFile("gamedata.xml")
    Parser.loadConfigFile("config.xml")
    Parser.loadKeywords()
    unittest.main()

