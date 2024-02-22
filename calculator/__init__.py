# Import necessary modules and classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(a, b, divide)
