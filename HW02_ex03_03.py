#!/usr/bin/env python
# HW02_ex03_03

# Python provides a built-in function called len that returns the length 
# of a string, so the value of len('allen') is 5.

# Write a function named right_justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the
# last letter of the string is in column 70 of the display.

# Example:
# >>> right_justify('allen')
#                                                                  allen
#                                                                 PYTHON
#                                                                PYTHON
################################################################################
# Write your function below:
# Body

def right_justify(name):
    length = len(name)
    init = ""
    for i in range(0,70-length):
        init = init + " " 
        
    print init + name
        
    print(" "*(70-len(name))+name)
    
    
# Write your function above:
################################################################################
def main():
    """Call your functions within this function."""
    print("Hello World!")
    right_justify("PYTHON")
    right_justify("POOJA")

if __name__ == "__main__":
    main()