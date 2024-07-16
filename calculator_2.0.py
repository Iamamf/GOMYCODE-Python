import math  # Importing the math module for advanced mathematical operations

class Calculator:
    def __init__(self):
        # Initializing the operations dictionary with basic operations and their corresponding methods
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
    
    def add(self, num1, num2):
        # Adding two numbers
        return num1 + num2
    
    def subtract(self, num1, num2):
        # Subtracting the second number from the first number
        return num1 - num2

    def multiply(self, num1, num2):
        # Multiplying two numbers
        return num1 * num2

    def divide(self, num1, num2):
        # Dividing the first number by the second number, with a check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 / num2
    
    def add_operation(self, symbol, function):
        # Adding a new operation to the operations dictionary
        self.operations[symbol] = function
    
    def calculate(self, num1, operation, num2):
        # Checking if the operation is valid
        if operation not in self.operations:
            print(f"Error: '{operation}' is not a valid operation.")
            return None
        
        # Checking if the inputs are numbers
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            print("Error: Both numbers must be integers or floats.")
            return None
        
        # Retrieving the function corresponding to the operation
        function = self.operations[operation]
        return function(num1, num2)  # Executing the function with num1 and num2 as arguments

# Creating an instance of the Calculator class
calc = Calculator()

# Defining functions for the advanced mathematical operations
def exponentiate(num1, num2):
    # Raising the first number to the power of the second number
    return num1 ** num2

def sqrt(num1, _):
    # Calculating the square root of the first number
    return math.sqrt(num1)

def logarithm(num1, num2):
    # Calculating the logarithm of num1 with base num2, with checks for valid inputs
    if num1 <= 0:
        print("Error: Logarithm base must be greater than 0.")
        return None
    if num2 <= 0 or num2 == 1:
        print("Error: Logarithm argument must be greater than 0 and not equal to 1.")
        return None
    return math.log(num1, num2)

# Adding advanced operations to the calculator
calc.add_operation('^', exponentiate)
calc.add_operation('sqrt', sqrt)
calc.add_operation('log', logarithm)

# Interactive loop to perform calculations
while True:
    # Prompting the user to enter the first number or exit the program
    num1_input = input("Enter the first number (or type 'exit' to quit): ")
    if num1_input.lower() == 'exit':
        break  # Exiting the loop if the user types 'exit'

    # Prompting the user to enter the operation
    operation = input("Enter the operation (+, -, *, /, ^, sqrt, log): ")

    # Prompting the user to enter the second number if needed
    num2_input = input("Enter the second number: ") if operation != 'sqrt' else '0'

    # Converting inputs to floats
    num1 = float(num1_input)
    num2 = float(num2_input)

    # Performing the calculation
    result = calc.calculate(num1, operation, num2)

    # Displaying the result if it's not None
    if result is not None:
        print(f"The result is: {result}")
