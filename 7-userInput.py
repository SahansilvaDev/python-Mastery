# input()



name = input("enter your name: ")
age = input("enter your age: ")

print(f"Name is {name}")
print(f"Age is {age}")

print(type(name)) #output: <class 'str'>
print(type(age)) #output: <class 'str'>

# so we get input in string format only so if we want to take number as input we have to convert it into int or float



name = input("enter your name: ")
age = int(input("enter your age: "))
score = float(input("enter your score: "))

print(f"Name is {name}")
print(f"Age is {age}")
print(f"Score is {score}")

print(type(name)) #output: <class 'str'>
print(type(age)) #output: <class 'int'>
print(type(score)) #output: <class 'float'>

# getting two numbers from user and printing their sum
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2
print(f"Sum is {sum}")