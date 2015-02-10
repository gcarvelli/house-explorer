import textwrap
import sys
from Utilities.Getch import Getch
#import curses

"""
Because Python's built-in print() function doesn't natively wrap, this function
takes any text, formats it correctly, and prints it to the screen. It is used
in place of print() throughout the program.
"""
def wrap(text):
    # force a string
    lines = textwrap.wrap(str(text), 79, replace_whitespace=False)
    for line in lines:
        print(line)

"""
http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user

Emulates python's input() statement, but handles command history under the hood.
"""
"""def getInput():
	string = ""
	previousChars = []

	c = ""

	while c != '\r':
		if(c != ""):
			#print(ord(c))
			printChar = False
			
			if(ord(c) == 3):
				# Ctrl + c
				sys.exit(1)
			elif(ord(c) == 127):
				# backspace
				if(len(string) > 0):
					string = string[:-1]
				printChar = True
			elif(ord(c) == 1):
				pass
			elif (c.isalnum() or c == ' ') and len(string) < 70:
				# character
				string += c
				printChar = True

			if(printChar):
				sys.stdout.write(c)
				sys.stdout.flush()
		c = Getch()
	sys.stdout.write('\n')
	sys.stdout.flush()
	return string


def clearLine(lengthOfLine):
	sys.stdout.write(chr(13)) # carriage return

	for i in range(0, 80):
		sys.stdout.write(' ') # space
	
	sys.stdout.write(chr(13)) # carriage return

	sys.stdout.flush()
"""