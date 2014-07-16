import textwrap

"""
Because Python's built-in print() function doesn't natively wrap, this function
takes any text, formats it correctly, and prints it to the screen. It is used
in place of print() throughout the program.
"""
def wrap(text):
    lines=textwrap.wrap(text, 79)
    for line in lines:
        print(line)
    