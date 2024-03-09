import sys
from app.commands import Command
from app.commands import CommandHandler

from calculator import Calculator
from decimal import Decimal, InvalidOperation


class CalculatorCommand(Command):
    def execute(self):
        print("Calculator App Started")
        while True:
            user_input = input("calc: ").strip()

            if user_input.lower() == 'exit':
                print("Exiting Calculator.")
                break

            try:
                a, b, operation = user_input.split()
                calculate_and_print(Decimal(a), Decimal(b), operation)
            except ValueError:
                print("Invalid input. Please enter a valid calculation.")
            except Exception as e:
                print(f"An error occurred: {e}")

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide,
        'power': Calculator.power,
        'root': Calculator.root
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()