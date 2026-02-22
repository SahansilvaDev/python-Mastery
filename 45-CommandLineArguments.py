# python test .py

# to run the python script file in command line or terminal
# we need to navigate to the directory where the script file is located 
# using cd command and then run the script file using python command followed by the script file name.
# for example if the script file is located in d:\Coding learning\Python\python-Mastery\45-CommandLineArguments.py
# then we need to navigate to d:\Coding learning\Python\python-Mastery using cd command and then run the script file using python command followed by the script file name.
# cd d:\Coding learning\Python\python-Mastery

# python 45-CommandLineArguments.py --num1 10 --num2 5 --operator +

# python 45-CommandLineArguments.py -n1 10 -n2 5 -op +

from argparse import ArgumentParser
from ast import operator



parser = ArgumentParser()

parser.add_argument("-n1","--num1", type=int, help="First number")
parser.add_argument("-n2","--num2", type=int, help="Second number")
parser.add_argument("-op","--operator", type=str, help="Operator (+, -, *, /)", choices=["+", "-", "*", "/"])

args = parser.parse_args()

print(args) # Namespace(num1=10, num2=5, operator='+')

num1 = args.num1
num2 = args.num2
operator = args.operator



if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result:", result)