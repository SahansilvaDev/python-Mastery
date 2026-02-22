# Decorators 

def divide(a, b):
    if b == 0:
        a,b = b,a
    return a / b

print(divide(10, 2))  # output: 5.0
print(divide(10, 0))  # output: 0.0, because the function is swapping a and b when b is zero, so it is returning 0 / 10 which is 0.0


# decorator function, it takes a function as an argument and 
# returns a new function that adds some functionality to the original function.
def divide(a, b):
    return a / b


def new(func): # decorator function
    def inner(a, b):
        if b == 0:
            a,b = b,a
        return func(a, b)
    return inner

new_divide = new(divide)  # new_divide is now a decorated version of the divide function
print(new_divide(10, 2))  # output: 5.0
print(new_divide(10, 0))  # output: 0.0, because the new_divide function is calling the inner function which is swapping a and b when b is zero, so it is returning 0 / 10 which is 0.0
print(new(divide)(30, 2))  # output: 15.0
print(new(divide)(30, 0))  # output: 0.0, because the new function is calling the inner function which is swapping a and b when b is zero, so it is returning 0 / 10 which is 0.0

#or


###################################################################


def new(func): # decorator function
    def inner(a, b):
        if b == 0:
            a,b = b,a
        return func(a, b)
    return inner


# @new - giving decorator function name with @ symbol before the function definition, 
# it is equivalent to new(divide)

@new # this is a decorator, it is equivalent to new(divide)
def divide(a, b):
    return a / b


print(divide(40, 2))  # output: 20.0
print(divide(10, 0))  # output: 0.0