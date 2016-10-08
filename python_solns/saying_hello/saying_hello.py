# This is the actual code for Exercise 1 of "Exercises for Programmers".
# Oct 12, 2016

import sys

def main():
    #main should go here
    name = ""
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = raw_input("Hi there, what's your name?")
    
    print(hello_str(name))


'''Utility function that returns a greeting string.'''
def hello_str(name=""):
    if name == "":
        return "Hello there, stranger!"
    elif name.lower() == "world":
        return "Hello world!"
    else:
        return "Hello there, {}!".format(name)

if __name__ == "__main__":
    main()
