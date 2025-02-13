#Data Types

# int - Integers  - Whole numbers - 1, 2, 3, 4, 5, 0, -1,-2,-3,-4,-5
# Float - Floats - Decimal numbers - 1.0, 2.0, 3.0, 4.0, 5.0, 0.0, -1.0,-2.0,-3.0,-4.0,-5.0
# Bool - Boolean - True or False
# complex - Complex numbers - 1+2j, 2+3j, 3+4j, 4+5j, 5+6j, 0+1j, -1+2j,-2+3j,-3+4j,-4+5j,-5+6j
# str - Strings - 'kamal', "python", "programming", "language", "data", "science", "machine", "learning"

# list - Lists - [1,2,3,4,5], - mutable - can change the values when running the program
# tuple - Tuples - (1,2,3,4,5) - immutable - we cannot change the values when running the program
# set - Sets - {1,2,3,4,5} - only contains unique values
# dict - Dictionaries - {'name': 'kamal', 'age': 20, 'weight': 56.2} - key-value pairs



# integer

a =10
b = -20
print(a)
print(type(a))
print(a.__sizeof__()) # 28 bytes


# float

a = 10.0
b = -20.0


# boolean - True or False need to be capitalised

a = True
b = False

# complex   
a = 1+2j
print(a)
print(type(a))
print(a.real)
print(a.imag)


#complex(1,2) is equivalent to 1+2j
#complex(real,imaginary)
a =complex(1,2)


# python is dynamically typed language - we don't need to specify the data type of the variable