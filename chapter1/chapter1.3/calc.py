import sys

def calculate(operator, num1, num2):
    """Performs a calculation based on the given operator and numbers.

    Args:
        operator (str): The operator to use (e.g., "+", "-", "*", "/").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the calculation.
    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calculator.py <operator> <num1> <num2>")
        sys.exit(1)

    operator = sys.argv[2]
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[3])

    result = calculate(operator, num1, num2)
    print(f"{num1} {operator} {num2} = {result}")