import textwrap

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
