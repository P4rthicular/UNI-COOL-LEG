Slist = []   # The main stack
Sname = None       # Stack name set to None to allow renaming, but only once
def StackCreate():   # Allows the name to be set, declaring the stack functional
    if Sname == None:
        Stacken()
    else:    # If the stack name has already been changed
        print("A stack currently exists.")

def Stacken():   # Allows user to set Sname, and acts as stack creation
    global Sname
    Sname = input("Please enter the new stack name:\n")
    
def StackAppend():   # Allows user to append an element to the stack
    if Sname != None:    # Function will not work if no Sname has been set
        addthis = input("Input element to be appended: ")
        Slist.append(addthis)    # Appends the input to stack
        print("Element",addthis,"appended to stack.")
        StackDisplay()  # Calls function to show the stack contents
    else:
        print("Not possible. Stack is missing.")

def StackRemove():   # Pops the Top element of the stack
    if len(Slist) != 0:  # Function will not work if there are no elements in stack
        Pcurrent = Slist.pop()   # removes the element
        print(Pcurrent,"removed from stack.")
        StackDisplay()   # Calls function to show the stack contents
    else:
        print("Not possible. Stack is empty or missing.")

def StackPeek():     # Shows the Top element of the stack
    if len(Slist) != 0:  # Function will not work if there are no elements in stack
        print("Showing the Top element of stack.")
        print(Slist[-1])     # Prints the most recently appended element
        StackDisplay()   # Calls function to show the stack contents
    else:
         print("Not possible. Stack is empty or missing.")

def StackDisplay():  # The function that shows the elements of the stack
    print("""------------------------
Displaying the contents of stack:""")
    if len(Slist) != 0:  # Function will not work if there are no elements in stack
        for count in reversed(Slist): # Prints the list of elements in reverse to emulate a stack
            print(count)
    else:
         print("Not possible. Stack is empty or missing.")

while True:  # Main interface of the program, allows the functions to be called
    print(f"""------------------------
Current Stack: {Sname} 
Choose an operation:
[C] Create a new stack
[A] Append to stack
[D] Pop from stack
[P] Peek Top element of stack
[S] Show stack element
Input 0 to quit.""") 
    ops = input()    # Input accepts both lower and uppercase version of specified letters
    if ops == "C" or ops == "c":     # Stack Creation
        StackCreate()
    elif ops == "A" or ops == "a":   # Stack Appending
        StackAppend()
    elif ops == "D" or ops == "d":   # Stack Popping
        StackRemove()
    elif ops == "P" or ops == "p":   # Stack Top Showing
        StackPeek()
    elif ops == "S" or ops == "s":   # Stack viewing
        StackDisplay()
    elif ops == "0":     # Ends the program
        break
    else:    # If any other input is entered other than the specified ones
        print("Input not recognized.")
        continue

 # Made by Manuel, Jillian Paul P.
 # October 28, 2023
