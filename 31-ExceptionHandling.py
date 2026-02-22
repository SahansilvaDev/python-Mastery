######################## Exception Handling ######################## 

# Exception handling is a mechanism to handle errors gracefully without crashing the program.
# It allows us to catch and handle exceptions (errors) that occur during the execution of a program.
# try-except block is used to handle exceptions in Python
# it occurs when users input something wrong or when we try to perform an operation that is not allowed, 
# such as dividing by zero or accessing an index that is out of range.
# that need to be handled by the programmer to prevent the program from crashing 
# and to provide a better user experience.


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
print(a/b) # this will raise a runtime error when user input 0 as the second number, 
# because division by zero is not allowed in mathematics and it will raise a ZeroDivisionError in Python.
print("thank you for using our program")

# Exception handling allows us to catch this error and handle it gracefully,
# so that the program does not crash and 
# we can provide a better user experience by showing a message to the user instead of crashing the program.



try: 
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except:
    print("Error: Division by zero is not allowed. Please enter a non-zero number as the second number.")
print("thank you for using our program")

# or

try: 
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except Exception as e: # showing occurred error message to the user
    print("Error:", e)
print("thank you for using our program")

# or

try: 
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except Exception as e:
    print("Error:", e)

finally: 
# this block will always execute regardless of whether an exception occurred or not, 
# it is used to perform cleanup actions such as closing files or releasing resources.
    print("thank you for using our program")



# we can also catch specific exceptions by specifying the exception type in the except block,
try: 
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero number as the second number.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("Error:", e)
finally:
    print("thank you for using our program")