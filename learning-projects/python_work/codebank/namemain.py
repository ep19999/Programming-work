#Use when want additional entry point for script. Make file accessable as standalone
#as well as imported module. eg. collecting user input when ran as a script

print(__name__, type(__name__))
if __name__ == "__main__":
    print("Nested code only runs in the top-level code environment")

# Collecting User input as argument with sys.argv object - list of strings representing all inputs
# Each word separated by whitespace in terminal input is counted as a new argument.

import sys
if __name__ == '__main__':
    text = " ".join(sys.argv[1:])
    print(function(text))
# run: python script.py argument argument


# Creating entry point for a package