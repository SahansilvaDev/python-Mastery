from calculator import *

num1 = 10
num2 = 0

addition = add(num1, num2)    # with two numbers
sub = subtract(num1, num2)    # with two numbers    
print(f"Addition: {addition}")  # Addition: 15
print(f"Subtraction: {sub}")    # Subtraction: 5

division = divide(num1, num2)    # with two numbers
print(f"Division: {division}")    # Division: Error: Division by zero is not allowed.
