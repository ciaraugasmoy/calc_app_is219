from decimal import Decimal
# Define the functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: Decimal, b: Decimal) -> Decimal:
    return a ** b

def root(a: Decimal, b: Decimal) -> Decimal:
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot calculate even root of a negative number")
    return a ** (Decimal('1') / b)