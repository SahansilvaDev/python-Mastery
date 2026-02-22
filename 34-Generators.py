# this is a simple function that returns the number 4 when called.
#  It is not a generator, but it serves as an example of a basic function in Python.
def test():
    return 4

print(test())  # output: 4

############# Generators #############

# A generator is a special type of iterator that allows you to iterate over a sequence of values
#  without storing them all in memory at once.
# Generators are defined using a function that contains one or more yield statements.
# The yield statement is used to produce a value and pause the function's execution,
# allowing it to be resumed later from the same point.

def test():
    yield 4

print(test()) # output: <generator object test at 0x7f8c8c8c8c8c>

y = test() # creating a generator object from the test function
print(next(y)) # output: 4

# when we call next() on the generator object, it executes the function 
# until it reaches the yield statement,
# returns the value (4 in this case), and pauses the function's execution.




def test(a):
    for i in a:
        yield i


y = test([1, 2, 3, 4]) # creating a generator object from the test function
print(next(y)) # output: 1
print(next(y)) # output: 2
print(next(y)) # output: 3
print(next(y)) # output: 4


'''
The line for _ in range(n): is a for loop that runs n times.
The underscore _ is used as a variable name when the value is not needed.
In this context, it means:
"Repeat the following code n times, but I don't care about the loop variable itself."

for _ in range(5):
    print("Hello")

'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fib(10):
    print(num) # output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# or can be written as this

def fib():
    a, b = 0, 1
    while True:
        c = a + b
        yield a
        a, b = b, c


y = fib()
print(next(y)) # output: 0
print(next(y)) # output: 1
print(next(y)) # output: 1
print(next(y)) # output: 2
print(next(y)) # output: 3


'''
Both versions of the fib generator are correct, but they serve different purposes:


1. fib(n) (with parameter)
Use this when you want a specific number of Fibonacci numbers.
It is safer and more practical for most use cases.
Example: for num in fib(10): print(num) prints the first 10 Fibonacci numbers.

2. fib() (infinite generator)
Use this when you want an infinite sequence and will control when to stop externally.
Useful for advanced cases, but can cause infinite loops if not handled carefully.
Example: next(y) repeatedly gives the next Fibonacci number forever.

'''