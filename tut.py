# Calculator
def addition(a, b):  # this function adds two numbers
    return a + b


def subtraction(a, b):  # this functions subtracts two numbers
    return a - b


def multiplication(a, b):  # this function multiplies two numbers
    return a * b


def division(a, b):  # this function divides two numbers
    return a / b


"""  Now we have to take input from users.
     First we have to tell user to select operations.
     Then we have to do calculations as the user selects the one operation
"""
operations = ['Addition', 'Subtraction',
              'Multiplication', 'Division']

User_Input = ""


# Using While loops for the whole operations
while User_Input != "quit":
    User_Input = input("Select the above operations(1/2/3/4): ")

    # If/elif/else statement
    if User_Input == "1":
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        print(num_1, " + ", num_2, " = ", addition(num_1, num_2))

    elif User_Input == "2":
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        print(num_1, " - ", num_2, " = ", subtraction(num_1, num_2))

    elif User_Input == "3":
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        print(num_1, " * ", num_2, " = ", multiplication(num_1, num_2))

    elif User_Input == "4":
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Enter another number: "))
        print(num_1, " / ", num_2, " = ", division(num_1, num_2))

    elif User_Input == "help":  # if the user get confused to select the operation
        print(""" Select 1 for addition \n
                  Select 2 for subtraction \n
                  Select 3 for multiplication \n
                  Select 4 for division \n
                  
            type quit to quit the calculator. 
        """)

    elif User_Input == "quit":
        print("See you soon! ")
        break
