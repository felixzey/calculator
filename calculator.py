import sys

print("Welcome to my first calculator v1.0")


def cont():
    ch = raw_input("Press x to exit, c to continue: ")
    if ch.lower() == 'c':
        pass
    else:
        sys.exit()


def read_input():
    x = input("First number: ")
    y = input("Second number: ")

    return [x, y]


def calculator():
    print("  A)Addition")
    print("  B)Subtraction")
    print("  C)Multiplication")
    print("  D)Division")
    x, y = read_input()
    choice = raw_input("Please pick a letter: ")
    if choice == "A" or choice == "a":
        print("Addition")
        print("Your answer is: " + str(x + y))
        #raw_input("Press <Enter> to exit")
        cont()
    elif choice == "B" or choice == "b":
        print("Subtraction")
        print("Your answer is: " + str(x - y))
        cont()
    elif choice == "C" or choice == "c":
        print("Multiplication")
        print("Your answer is: " + str(x * y))
        cont()
    elif choice == "D" or choice == "d":
        print("Division")
        try:
            ans = x / y
            print("Your answer is: " + str(ans))
        except:
            print 'You can\'t divide by 0 or do other stupid things'
        cont()
    else:
        print("Please make a valid choice. Please try again")

while True:
    calculator()
