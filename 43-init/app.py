import calculator

# from calculator import add


print(type(calculator)) # <class 'module'>
print(calculator) # <module 'calculator' from 'd:/Coding learning/Python/python-Mastery/43-init/calculator.py'>

print(calculator.add(2, 3))    # with two numbers

from calculator import subtract

print(subtract(5, 2))    # with two numbers

from calculator import *  # import all functions from calculator module

addition = add(10, 20)    # with two numbers
sub = subtract(15, 5)    # with two numbers   

print(f"Addition: {addition}")  # Addition: 30
print(f"Subtraction: {sub}")    # Subtraction: 10


from SumText import add as add_txt

add_txt("Hello, ", "World!")  # Adding text: Hello, World!



# from package1.module1 import fun1
# from package1.module1 import fun2

# fun1()  # Function 1 from module1 in package1
# fun2()  # Function 2 from module2 in package1


import numpy as np
import time

# using init file to import functions from module1 and module2 in package1
import package1
package1.fun1()  # Function 1 from module1 in package1
package1.fun2()  # Function 2 from module2 in package1


package1.package_fun()  # Function in package1 from init file

