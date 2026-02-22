# funtions
# 1 - Built-in functions
# 2 - User-defined functions

# Built-in functions
# print() , type(), len(), input(), str(), int(), float(), bool(), list(), dict(), set(), tuple(), range(), sum(), min(), max(), abs(), round()


help(pow)  # shows the documentation of the function

result = pow(2, 3)  # 2 raised to the power of 3
print(result)  # output: 8

result = abs(-10)  # absolute value
print(result)  # output: 10

result = round(3.14159, 2)  # round to 2 decimal places
print(result)  # output: 3.14

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)  # sum of the list
print(total)  # output: 150

minimum = min(numbers)  # minimum value in the list
print(minimum)  # output: 10

maximum = max(numbers)  # maximum value in the list
print(maximum)  # output: 50

# converting data types
num_str = "123"
num_int = int(num_str)  # convert string to integer
print(num_int)  # output: 123

num_float = float(num_str)  # convert string to float
print(num_float)  # output: 123.0

bool_value = bool(num_int)  # convert integer to boolean
print(bool_value)  # output: True

str_value = str(num_int)  # convert integer to string
print(str_value)  # output: "123"

import math # for more mathematical functions
print(math.sqrt(16)) # output: 4.0
print(math.ceil(4.3)) # output: 5
print(math.floor(4.7)) # output: 4
print(math.factorial(5)) # output: 120
print(math.gcd(48, 18)) # output: 6
print(math.sin(math.pi/2)) # output: 1.0
print(math.cos(0)) # output: 1.0
print(math.log(100, 10)) # output: 2.0
print(math.exp(2)) # output: 7.38905609893065


import random # for random number functions
print(random.randint(1, 10)) # output: random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry'])) # output: random choice from the list
print(random.random()) # output: random float between 0.0 and 1.0

import datetime # for date and time functions - this is module datetime
now = datetime.datetime.now()
print(now) # output: current date and time
print(now.year) # output: current year
print(now.month) # output: current month
print(now.day) # output: current day
print(now.hour) # output: current hour
print(now.minute) # output: current minute
print(now.second) # output: current second
print(now.strftime("%Y-%m-%d %H:%M:%S")) # output: formatted date and time










