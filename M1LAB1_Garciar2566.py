 # -*- coding: utf-8 -*-
"""
# CSC 221
# M1LAB1 - Double a Number
# Rebecca Garcia
# 18082021
"""

entered = [] # global ... for now
doubled = [] # global ... for now


def main():
        """Main Loop of program."""
        print("\nThis is \"Double A #\" program.")
        
        repeat = True
        while repeat == True:
        # TODO: This should loop
       
            collectUserInput()
            repeat = repeatOrNot()
        print("Goodbye!") #U+1F913
        print("#\'s Entered:", entered)
        print("#\'s Doubled:", doubled)
        
        
def collectUserInput():
    """Ask for input, double it, print result"""
    num = int(input("Enter a number: "))
    dbl = doubleNumber(num)
    entered.append(num)
    doubled.append(dbl)
    print(num, "doubled is:", dbl,"\n")
    
def doubleNumber(num):
    result = num * 2
    return result #TODO make this actually work
    
def repeatOrNot():
    """input: one number.
    output. the number * 2."""
     
    print("1. Enter another number")
    print("2. Exit")
    
    goAgain = int(input("> "))
    if 1 == goAgain:
        return True
    return False

# traditional magic to invoke main
if __name__ == "__main__":
    main()
    
        
        