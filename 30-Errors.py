################### Types of Errors in Python ###################

# Syntax Error - occurs when the code is not written in the correct syntax
# print("Hello World"  # missing closing parenthesis - SyntaxError: unexpected EOF while parsing








# 2. Name Error - occurs when we try to use a variable that has not been defined
# print(x) # NameError: name 'x' is not defined

# 3. Type Error - occurs when we try to perform an operation on a variable of the wrong type
# x = 5 + "Hello" # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 4. Index Error - occurs when we try to access an index that is out of range
# my_list = [1, 2, 3]
# print(my_list[3]) # IndexError: list index out of range

# 5. Key Error - occurs when we try to access a key that does not exist in a dictionary
# my_dict = {"name": "Sahan", "age": 30}
# print(my_dict["city"]) # KeyError: 'city'

# 6. Attribute Error - occurs when we try to access an attribute that does not exist
# my_list = [1, 2, 3]
# my_list.append(4) # this is correct
# my_list.add(5) # AttributeError: 'list' object has no attribute 'add'

# 7. Value Error - occurs when we try to convert a value to a type that is not compatible
# x = int("Hello") # ValueError: invalid literal for int() with base 10: 'Hello'





# logical errors - occurs when the code runs without any error but produces incorrect results
# x = 10
# y = 5
# result = x - y # logical error, should be x + y
# print(result) # output: 5, but it should be 15

# print(10+20*2) really want to get 60 but it will give 50 because of operator precedence, 
# this is a logical error

# need logical error to be fixed by the programmer,
#  it cannot be detected by the interpreter or compiler, 
# it can only be detected by testing the code and checking the output

# print((10+20)*2) 


# runtime errors - occurs when the code runs and encounters an error during execution
# this can occurs when users getting inputs
# x = 10
# y = 0
# result = x / y # runtime error, ZeroDivisionError: division by zero

# 8. ZeroDivisionError - occurs when we try to divide a number by zero
# x = 10 / 0 # ZeroDivisionError: division by zero 













