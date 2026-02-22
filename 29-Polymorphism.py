# poymorphism - many forms

# method overriding - same method name with same parameters
# method overloading - same method name with different parameters
# operator overloading - same operator with different operands

# operator is a symbol that performs a specific operation on one or more operands and 
# produces a result eg +, -, *, /, etc.

# operands are the values on which the operator performs the operation 
# eg 2 + 3, here + is the operator and 2 and 3 are the operands


print("######################  Operator overriding  ######################")

# method overriding - same method name with same parameters
class MobilePhone:
    def send_message(self, name):
        print(f"Hello, this is a message from your mobile phone {name}.")

class SmartPhone(MobilePhone):
    def send_message(self, name):
        print(f"Hello, this is a message from your smart phone {name}.")

phone1 = MobilePhone()
phone1.send_message("Apple")

phone2 = SmartPhone() # phone2 is an object of SmartPhone class to access attributes and methods and constructors method is SmartPhone()
phone2.send_message("Samsung")




# method overloading - same method name with different parameters

# In Python, method overloading (having multiple methods with the same name but different parameters) 
# is not supported in the same way as languages like Java or C++. If you define multiple methods with
#  the same name in a class, only the last one will be used.

''' 
However, you can achieve similar behavior using,

Default arguments
Variable-length arguments (*args and **kwargs)
Type checking inside the method

'''
print("######################  Operator Overloading - default arguments  ######################")


# default arguments
class MobilePhone:
    def send_message(self, name, age=None):
        if age is not None:
            print(f"Hello, this is a message from your mobile phone {name} and you are {age} years old.")
        else:
            print(f"Hello, this is a message from your mobile phone {name}.")

phone1 = MobilePhone()
phone1.send_message("Apple", 25)   # with age
phone1.send_message("orange")      # without age

#or

class calculator:
    def add(self, a=None, b=None,c=None):
        sum = 0
        if a!= None and b!= None and c!= None:
            sum = a + b + c
            print(f"The sum of three numbers is: {sum}")
        elif a!= None and b!= None:
            sum = a + b
            print(f"The sum of two numbers is: {sum}")
        else:
            sum = a
            print(f"The number is: {sum}")

calc = calculator()
calc.add(2, 3, 4) # with three numbers
calc.add(2, 3)    # with two numbers
calc.add(2)       # with one number



print("######################  Operator Overloading - *args - variable-length arguments  ######################")


# *args - variable-length arguments
class MobilePhone:
    def send_message(self, name, *args):
        if args:
            print(f"Hello, this is a message from your mobile phone {name} and you are {args[0]} years old.")
        else:
            print(f"Hello, this is a message from your mobile phone {name}.")

phone1 = MobilePhone()
phone1.send_message("Apple", 25)   # with age
phone1.send_message("Apple", 25, 30)   # with age
phone1.send_message("orange")      # without age
#or 

# variable-length arguments
class MobilePhone:
    def send_message(self, *names):
        for name in names:
            print(f"Hello, this is a message from your mobile phone {name}.")


phone1 = MobilePhone()
phone1.send_message("Apple", "Samsung", "OnePlus") # with multiple names


print("######################  Operator Overloading - Type checking inside the method  ######################")
# Type checking inside the method
class MobilePhone:
    def send_message(self, name, age=None):
        if isinstance(age, int):
            print(f"Hello, this is a message from your mobile phone {name} and you are {age} years old.")
        else:
            print(f"Hello, this is a message from your mobile phone {name}.")

phone1 = MobilePhone()
phone1.send_message("Apple", 25)   # with age
phone1.send_message("orange", "twenty five")      # with age as string, will not print age

#isinstance() function is used to check the type of the variable and 
# it returns True if the variable is of the specified type and False otherwise.


print("######################  Operator Overloading  ######################")

# Operator overloading allows you to define how operators like +, -, *, etc., 
# behave for your own classes.

# For example, you can make the + operator add two objects of your class in a custom way.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# The __add__ method is a special method that is called when the + operator is used with objects of the class.
# In this case, it takes another Point object as an argument and returns a new Point object with 
# the x and y values added together.


    # Overload the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
# The __str__ method is a special method that is called when the object is printed.
# It returns a string representation of the object.
# __str__ meaning is to return a string representation of the object when we print it. 
# It is used to define how the object should be represented as a string.
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This uses the __add__ method

print(p3)  # Output: (4, 6)

p4 = Point(str(1), str(2))
p5 = Point(str(3), str(4))
p6 = p4 + p5  # This will concatenate the strings
print(p6)  # Output: (13, 24)

p7 = Point("Hello", "World")
p8 = Point(" ", " ")
print(p7) # Output: (Hello, World)
print(p8) # Output: ( ,  ) this uses the __str__ method to print the point as a string