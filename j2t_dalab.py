# Program 1 
#A Program that asks for an array within 5-10 elements and returns all numbers larger than 10
def program1():
    ary = []
    bigary = []
    halp = 0
    long1 = int(input("Please enter the size of your array. Between 5-10 elements:"))
    while long1 != halp - 1:
        if long1 < 5 or long1 > 10:
            print("Invalid length.")
            continue
        else:
            for _ in range(long1):
                pend = int(input("Enter an integer:"))
                ary.append(pend)
            while halp != long1:
                if ary[halp] > 10:
                    new = ary[halp]
                    bigary.append(new)
                halp += 1
        print("Your list is:", ary)
        print("The numbers you gave that are larger than 10 are:", bigary)
        break

# Program 2
# A Program that asks for a string and determines if it is a palindrome
# A palindrome is a word that reads the same word if spelled backwards
def program2():
    darome = input("Please give a word to be checked as a palindrome:")
    pal = list(darome)
    if pal == list(reversed(pal)):
        print("Your word is a palindrome.")
    else:
        print("Your word is not a palindrome.")

# Program 3
# A program that checks input by end-user, if input is 1, ask for integer and loop. If 0, display array and end.
def program3():
    cycle = []
    while True:
        loop = int(input("Please press 1 to loop, or 0 to end:"))
        if loop == 1:
            bol = int(input("Please enter an integer.:"))
            cycle.append(bol)
            continue
        elif loop == 0:
            print("Loop ended. Displaying array of given integers.")
            print(cycle)
            break
        else:
            print("Invalid input")
            continue

while True:
    print("----------------------------------------------------------")
    print("Please choose the number of the program you want to run:")
    print("[1] A Program that asks for an array within 5-10 elements and returns all numbers larger than 10.")
    print("[2] A Program that asks for a string and determines if it is a palindrome.")
    choice = int(input("[3] A program that checks input by end-user, if input is 1, ask for integer and loop. If 0, display array and end.\n" ))
    if choice == 1:
        program1()
    elif choice == 2:
        program2()
    elif choice == 3:
        program3()
    else:
        print("Invalid option.")
        continue
          
# Made by Jillian Paul Manuel
# September 13, 2023
