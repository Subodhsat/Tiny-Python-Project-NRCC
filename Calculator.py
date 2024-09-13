#############     CALCULATOR     #######################

def calculator(operation, *args):

    # Validate number of operands
    if len(args) != 2:
        raise ValueError("Exactly two operands are required.")
    
    a, b = args
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("Operands must be integers or floats.")
    

    # Perform the operation
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation. Use 'add', 'subtract', 'multiply', or 'divide'.")


# Input taken from the user 
try:
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))
    
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    # strip and lower strips the space and lower the characters respectively

    # Call the calculator function with the user input
    result = calculator(operation, number_1, number_2)
    print(f"The result of {operation} is: {result}")

except ValueError as e:
    print(f"Error: {e}")
