 ###################### Lists Data Type ######################

# Lists is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets [].
# Lists is mutable - we can change, add, remove items after the list has been created. and when running the code.



lst =  ["sad", "mad", "glad"]
print(lst) # output: ['sad', 'mad', 'glad']

lst2 = list(("sad", "mad", "glad"))
print(lst2) # output: ['sad', 'mad', 'glad']

list3 = [1, 2.5, "hello", True, [1, 2, 3]]
print(list3) # output: [1, 2.5, 'hello', True, [1, 2, 3]]
print(type(list3)) # output: <class 'list'>
print(len(list3)) # output: 5
print(list3[0]) # output: 1
print(list3[2]) # output: hello
print(list3[-1]) # output: [1, 2, 3]
print(list3[4][1]) # output: 2
print(list3[1:4]) # output: [2.5, 'hello', True]

# list slicing
print(list3[::2]) # output: [1, 'hello', [1, 2, 3]]
print(list3[::-1]) # output: [[1, 2, 3], True, 'hello', 2.5, 1]


# list concatenation
list4 = [4, 5, 6]
combined_list = list3 + list4
print(combined_list) # output: [1, 2.5, 'hello', True, [1, 2, 3], 4, 5, 6]  


# in and not in operators
print(2.5 in list3) # output: True
print("world" not in list3) # output: True


# list methods
fruits = ["apple", "banana", "cherry"]

fruits.append("orange") # adds item to the end
print(fruits) # output: ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi")
print(fruits) # output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana") # removes first occurrence of item
print(fruits) # output: ['apple', 'kiwi', 'cherry', 'orange']

fruits.pop() # removes last item .pop(index) can remove item at specific index
print(fruits) # output: ['apple', 'kiwi', 'cherry']

fruits.sort()
print(fruits) # output: ['apple', 'cherry', 'kiwi']

fruits.reverse()
print(fruits) # output: ['kiwi', 'cherry', 'apple']

fruits.remove("cherry")
print(fruits) # output: ['kiwi', 'apple']


numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()
print(numbers) # output: [1, 2, 5, 5, 6, 9]

numbers.reverse()
print(numbers) # output: [9, 6, 5, 5, 2, 1]

numbers.clear()
print(numbers) # output: []

# copy()
original = ["a", "b", "c"]
copied = original.copy()
print(copied) # output: ['a', 'b', 'c']

# count()
letters = ["a", "b", "a", "c", "a"]
print(letters.count("a")) # output: 3

# extend()
listA = [1, 2, 3]
listB = [4, 5, 6]
listA.extend(listB)
print(listA) # output: [1, 2, 3, 4, 5, 6]
#append vs extend - append can only include one item at a time where extend can include multiple items at once

listC = ["x", "y"]
print(listA) # output: [1, 2, 3, 4, 5, 6]
listA.extend(listC) # or listA = listA + listC or listA += listC or listA.extend(["x", "y"])
print(listA) # output: [1, 2, 3, 4, 5, 6, 'x', 'y']


# index()
colors = ["red", "green", "blue"]
print(colors.index("green")) # output: 1


# List is mutable - means we can change items when running the code
numbers = [10, 20, 30, 40, 50]
print(numbers) # output: [10, 20, 30, 40, 50]
numbers[2] = 35
print(numbers) # output: [10, 20, 35, 40, 50]