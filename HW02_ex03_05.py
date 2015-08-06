#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


str1 = "+"
str2 = "- - - -"
str3 = "|"
str4 = "       "


def M1(cols):
    print str1,
    for i in range(0,cols):
        print str2,str1,
    
    print 
    
def M2(cols, rows):
        for i in range (0, cols+2):
            for j in range(0, rows+1):
                print str3, str4,
            print

    
def two_by_two():
    M1(2)
    M2(2,2)
    M1(2)
    M2(2,2)
    M1(2)
    
    
def four_by_four():
    M1(4)
    M2(2,4)
    M1(4)
    M2(2,4)
    M1(4)
    M2(2,4)
    M1(4)
    M2(2,4)
    M1(4)
            
            
      
      
    
    
    
    






# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    two_by_two()
    four_by_four()
    



if __name__ == "__main__":
    main()