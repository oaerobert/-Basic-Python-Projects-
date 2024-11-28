# Define basic mathematical functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Undefined"

# Main program starts here
print(f'Welcome to the Calculator!')
print(f"Firstly, select a number from the list below. If you haven't exited, you will be asked to input two numbers of choice!")
print(f'    1. Addition')
print(f'    2. Subtraction')
print(f'    3. Division')
print(f'    4. Multiplication')
print(f'    5. Exit program')

# Loop to keep the calculator running until the user exits/finishes
while True:
    try:
        # Get the user's choice
        choice = float(input(f"Select your chosen number from the list (1/2/3/4/5): "))
        # If user enters a number not within the list
        if choice not in [1,2,3,4,5]:
            print(f"Please try again, and select a number from within this list.")
            continue
        # If user decides to exit the program
        if choice == 5:
            print(f'Exited program. Goodbye!')
            break
        # Get the numbers for the calculation
        number1 = float(input(f"Now, enter your first number: "))
        number2 = float(input(f"And enter your second number: "))
        # Perform chosen operation
        if choice == 1:
            print(f'The sum of your numbers are: {add(number1, number2)}')
            break

        elif choice == 2:
            print(f'Subtracting both numbers gives you: {subtract(number1, number2)}')
            break

        elif choice == 3:
            print(f'Dividing your numbers give: {divide(number1, number2)}')
            break

        elif choice == 4:
            print(f'Multiplying your numbers give: {multiply(number1, number2)}')
            break
    except ValueError:
        # Handle invalid inputs for numbers or choices
        print("Invalid Input, Try Again. Please Enter a Valid Number.")
