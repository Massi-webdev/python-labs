# This the lab 3 assignment
"""
1. A function that takes a name as input and prints an introduction line.
2. Includes comments and uses input/output functions.
"""
def write_intro(name):
    """Displays a personalized greeting."""
    print('Hello', name)

write_intro(input('What is your name?'))