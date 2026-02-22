# lamda is an anonymous function, it is a function without a name, this is python's way of creating a function without a name, 
# it is also called a lambda function, it is used to create small, one-time, anonymous functions, 
# it is often used in conjunction with the map(), filter(), and reduce() functions.
# lamda is keyword, it is used to create a lambda function, it is followed by the parameters, then a colon, 
# and then the expression, the expression is evaluated and returned when the lambda function is called.

# normal function
def area(x):
    return x * x

print(area(5))  # output: 25

# using lambda function
#argument x is passed to the lambda function, and the expression x * x is evaluated and returned when the lambda function is called.
# lamda, argument(s) : expression

area_lambda = lambda x: x * x
print(area_lambda(5))  # output: 25 

# using lambda function with multiple arguments
add = lambda x, y: x + y
print(add(5, 3))  # output: 8

# In the lambda function definition (lambda x, y: x + y), x and y are parameters. 
# When you call add(5, 3), 5 and 3 are arguments. 
# Parameters are the names listed in the function definition; 
# arguments are the values passed to the function when it is called.


def apple(unitPrice):
    return lambda quantity: unitPrice * quantity

x = apple(10)  
# x is now a lambda function that takes quantity as an argument and returns unitPrice * quantity
print(x(5))  # output: 50, because x(5) is equivalent to 10 * 5



# using lambda function with map() function - map() function is used to apply a function to all 
# the items in an iterable (list, tuple etc.) 
# and return a map object (which is an iterator) of the results.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # output: [2, 4, 6, 8, 10], because the lambda function is multiplying each element in the numbers list by 2


# using lambda function with filter() function
# filter() function is used to filter the items in an iterable (list, tuple etc.) 
# based on a function that returns True or False, and return a filter object (which is an iterator) of 
# the items that satisfy the condition.

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # output: [2, 4]

# or


def even(x):
    return x % 2 == 0

y = list(filter(even, numbers))
print(y)  # output: [2, 4]



# reduce() function is used to apply a function of 
# two arguments cumulatively to the items of an iterable from left to right,
# so as to reduce the iterable to a single value. 
# For example, if you want to calculate the product of all numbers in a list, 
# you can use reduce() function with a lambda function.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # output: 120, because 1 * 2 * 3 * 4 * 5 = 120
