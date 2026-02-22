# funtions - procedure programming
# 1 - Built-in functions
# 2 - User-defined functions

# User-defined functions


# def function_name(parameters):
#     """docstring"""
#     # function body
#     pass
# function_name(arguments)  # function call

def greet(name):
    """This function greets the person passed as a parameter."""
    print("Hello, " + name + "! Welcome to Python programming.") #or 
    print(f"Hello, {name}! Welcome to Python programming.")
greet("Sahan")
# output:
# Hello, Sahan! Welcome to Python programming.
# Hello, Sahan! Welcome to Python programming.

def sum_num(a,b):
   return a+b

sum_result = sum_num(10, 20)
print("Sum:", sum_result)  # output: Sum: 30

def sum_num(a,b):
   print(a+b) # print the sum instead of returning it

sum_result = sum_num(10, 20)

def func(length,width):
   area = length * width
   perimeter = 2 * (length + width)
   print("Area:", area)
   print("Perimeter:", perimeter)

func(5, 10)
# output: 
# Area: 50
# Perimeter: 30

func(5, 10)
# output: 
# Area: 50
# Perimeter: 30

def sum_numbers(*args):
    """This function returns the sum of all numbers passed as arguments."""
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)

print("Total Sum:", result)  # output: Total Sum: 15



def student(sub1,marks):
    print("Subject:", sub1)
    print("Marks:", marks)

student(marks=85, sub1="Maths")

# output:
# Subject: Maths
# Marks: 85


def student(sub1="Maths",marks=85):
    print("Subject:", sub1)
    print("Marks:", marks)

student("science", 90)


# output:
# Subject: science
# Marks: 90

def student(sub1="Maths",marks=85):
    print("Subject:", sub1)
    print("Marks:", marks)

student("science")# getting default marks when not passed argument

# output:
# Subject: science
# Marks: 85



def student(sub1,marks,*friends): #*friends mean we can not say exactly how many arguments will be passed
    print("Subject:", sub1)
    print("Marks:", marks)
    print("Friends:", friends)

student("science", 90,"elon", "bill", "steve") 

# output:
# Subject: science
# Marks: 90
# Friends: ('elon', 'bill', 'steve')


def student(sub1,marks,**friends): # **friends mean we want to add dictionary type arguments 
    print("Subject:", sub1)
    print("Marks:", marks)
    print("Friends:", friends)
    for key, value in friends.items():
        print(f"Friend Name: {key}, Age: {value}")

student("science", 90,elon=20, bill=30, steve=40) 

# output:
# Subject: science
# Marks: 90
# Friends: {'elon': 20, 'bill': 30, 'steve': 40}
# Friend Name: elon, Age: 20
# Friend Name: bill, Age: 30
# Friend Name: steve, Age: 40





# Types of Arguments in Python
# 1 - Positional Arguments
# 2 - Keyword Arguments
# 3 - Default Arguments
# 4 - Variable-length Arguments




# 1 - Positional Arguments - need careful about the order of arguments when calling the function
def student(sub1,marks):
    print("Subject:", sub1)
    print("Marks:", marks)

student("Maths", 85) # need careful about the order of arguments when calling the function

# 2 - Keyword Arguments - we can specify the parameter name when calling the function   
def student(sub1,marks):
    print("Subject:", sub1)
    print("Marks:", marks)

student(marks=85, sub1="Maths") # we can specify the parameter name when calling the function 



# 3 - Default Arguments - we can assign default values to parameters in the function definition
def student(sub1="Maths",marks=85):
    print("Subject:", sub1)
    print("Marks:", marks)

student() # getting default values when not passed arguments
student("science")# getting default marks when not passed argument
student("science", 90) # overriding default values by passing arguments

# or

def student(sub1,marks=85):
    print("Subject:", sub1)
    print("Marks:", marks)

student("science")# getting default marks when not passed argument
student("science", 90) # overriding default marks by passing argument


# 4 - Variable-length Arguments

# def total_marks(*args): #*args mean we can not say exactly how many arguments will be passed
def total_marks(*marks): #*marks mean we can not say exactly how many arguments will be passed
    total = 0
    for mark in marks:
        total += mark
    print("Total Marks:", total)


total_marks(85, 90, 78, 92) # getting value as tuple
# output: Total Marks: 345
# we can pass any number of arguments

def total_marks(**kwargs): #**kwargs mean we want to add dictionary type arguments
    total = 0
    for mark in kwargs.values():
        total += mark
    print("Total Marks:", total)
    print("Details:", kwargs)

total_marks(maths=85, science=90, english=78, history=  92) # getting value as dictionary
# we can pass any number of arguments as dictionary type
# output:
# Total Marks: 345
# Details: {'maths': 85, 'science': 90, 'english': 78, 'history': 92}