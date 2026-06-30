def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Error! Division by zero is not allowed.")
    return x / y

def get_number(prompt):
    """Prompts the user to enter a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Prompts the user to select an arithmetic operation."""
    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide)
    }
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    while True:
        choice = input("Enter choice (1/2/3/4) or the operator (+/-/*//): ").strip()
        if choice in operations:
            return operations[choice]
        # Check if they entered the symbol directly
        for key, val in operations.items():
            if choice == val[0]:
                return val
        print("Invalid choice. Please enter a valid option (1, 2, 3, 4) or operator (+, -, *, /).")

def format_number(val):
    """Formats float number to int if it represents an integer, to keep output clean."""
    return int(val) if val.is_integer() else val

def main():
    print("=== Simple CLI Calculator ===")
    
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        op_symbol, op_func = get_operation()
        
        try:
            result = op_func(num1, num2)
            
            # Format inputs and result nicely for display
            num1_display = format_number(num1)
            num2_display = format_number(num2)
            result_display = format_number(result)
                
            print(f"\nResult: {num1_display} {op_symbol} {num2_display} = {result_display}")
        except ValueError as e:
            print(f"\n{e}")
            
        print("\n" + "-"*30)
        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice not in ('y', 'yes'):
            print("Thank you for using Simple Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
