def calculator():
    """
    Simple Calculator:
    Performs basic arithmetic operations (+, -, *, /) 
    with user input and validates inputs.
    """

    print("🔢 Welcome to the Command Line Calculator!")
    print("You can perform operations: +  -  *  /")
    print("Let's get started!\n")

    cal_on = True
    while cal_on:

        num1 = float(input('Please enter your first number: '))
        operation = input('Please choose the operation (+,-,*,/): ')
        num2 = float(input('Please enter your second number: '))
        
        if operation not in '+-*/':
            print("Choose a valid operation from the given (+, -, *, /)")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Number two cannot be zero for division"

        print(f'Result: {num1}  {operation}  {num2} = {result}')
            
        choice = input('Do you want to continue(y/n): ')
        if choice.lower() != 'y':
            cal_on = False
            print("GoodBye!")