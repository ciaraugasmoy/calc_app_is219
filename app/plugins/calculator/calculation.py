
# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable
# Import arithmetic operations from a module named calculator.operations
from calculator.operations import *

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    # Constructor method with type hints for parameters and the return type
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Initialize the first operand of the calculation
        self.a = a
        # Initialize the second operand of the calculation
        self.b = b
        # Store the operation as a callable that takes two Decimals and returns a Decimal
        # This allows for flexible assignment of any function that matches this signature (like add, subtract, etc.)
        self.operation = operation
    
    # Static method to create a new instance of Calculation
    # This method provides an alternative constructor that can be used without instantiating the class directly
    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Return a new Calculation object initialized with the provided arguments
        return Calculation(a, b, operation)

    # Method to perform the calculation stored in this object
    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        # The operation (e.g., add, subtract) is called with the operands (a and b) and the result is returned
        return self.operation(self.a, self.b)

    # Special method to provide a string representation of the Calculation instance
    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        # This method makes it easier to understand what the Calculation object represents when printed or logged
        # The operation.__name__ attribute is used to get the function's name for a more readable output
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
