 ###################### Tuples Data Type ######################

# Tuples is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are written with round brackets ().
# Tuples is immutable - we cannot change, add, remove items after the tuple has been created. and when running the code.

tpl =  ("sad", "mad", "glad")
print(tpl) # output: ('sad', 'mad', 'glad')
tpl2 = tuple(("sad", "mad", "glad"))
print(tpl2) # output: ('sad', 'mad', 'glad')

tpl3 = (1, 2.5, "hello", True, [1, 2, 3])
print(tpl3) # output: (1, 2.5, 'hello', True, [1, 2, 3])
print(type(tpl3)) # output: <class 'tuple'>
print(len(tpl3)) # output: 5
print(tpl3[0]) # output: 1
print(tpl3[2]) # output: hello
print(tpl3[-1]) # output: [1, 2, 3]
print(tpl3[4][1]) # output: 2
print(tpl3[1:4]) # output: (2.5, 'hello', True)

# tuple slicing
print(tpl3[::2]) # output: (1, 'hello', [1, 2, 3])
print(tpl3[::-1]) # output: ([1, 2, 3], True, 'hello', 2.5, 1)

# tuple concatenation
tpl4 = (4, 5, 6)
combined_tpl = tpl3 + tpl4
print(combined_tpl) # output: (1, 2.5, 'hello', True, [1, 2, 3], 4, 5, 6)

# in and not in operators
print(2.5 in tpl3) # output: True
print("world" not in tpl3) # output: True

# tuple methods
num_tpl = (5, 2, 9, 1, 5, 6)
print(num_tpl.count(5)) # output: 2
print(num_tpl.index(9)) # output: 2



# unpacking tuples
coordinates = (10, 20, 30)
x, y, z = coordinates  
print(x) # output: 10
print(y) # output: 20
print(z) # output: 30


a, b, c, d, e = ("red", "green", "blue", "yellow", "purple")
print(a) # output: red
print(b) # output: green
print(c) # output: blue
print(d) # output: yellow    

# using * to unpack
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
a, b, *rest = fruits
print(a) # output: apple
print(b) # output: banana
print(rest) # output: ['cherry', 'orange', 'kiwi']

*a, b, c = fruits
print(a) # output: ['apple', 'banana', 'cherry']
print(b) # output: orange
print(c) # output: kiwi

# list convertion to tuple
my_list = [1, 2, 3, 4, 5]

my_tuple = tuple(my_list)
print(my_tuple) # output: (1, 2, 3, 4, 5)

# tuple convertion to list
my_new_list = list(my_tuple)
print(my_new_list) # output: [1, 2, 3, 4, 5]


# tuple convertion to string
my_string = str(my_tuple)
print(my_string) # output: (1, 2, 3, 4, 5)
print(type(my_string)) # output: <class 'str'>