import math
import sys

print("Welcome to my first calculator v1.0")

def cont():
    ch = raw_input("Press x to exit, c to continue: ")
    if ch.lower() == 'c':
	pass
    else:
	sys.exit()


def calculator():
    print("  A)Addition")
    print("  B)Subtraction")
    print("  C)Multiplication")
    print("  D)Division")
    choice = raw_input("Please pick a letter: ")
    if choice == "A" or choice == "a":
        print("Addition")
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Your answer is: " + str(x + y))
        #raw_input("Press <Enter> to exit")
	cont()
    elif choice == "B" or choice == "b":
        print("Subtraction")
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Your answer is: " + str(x - y))
	cont()
    elif choice == "C" or choice == "c":
        print("Multiplication")
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Your answer is: " + str(x * y))
	cont()
    elif choice == "D" or choice == "d":
        print("Division")
        x = input("First Number: ")
        y = input("Second Number: ")
        print("Your answer is: " + str(x / y))
	cont()
    else:
        print("Please make a valid choice. Please try again")

while True:
    calculator()
