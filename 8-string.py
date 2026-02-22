###################### Strings Data Type ######################

from posixpath import split


name = "Sahan Silva"

print(name)  # output: Sahan Silva
print(type(name))  # output: <class 'str'>


print(name[0])  # output: S
print(name[1])  # output: a
print(name[2])  # output: h
print(name[3])  # output: a
print(name[4])  # output: n
print(name[5])  # output:
print(name[6])  # output: S
print(name[7])  # output: i
print(name[8])  # output: l
print(name[9])  # output: v
print(name[10])  # output: a
# print(name[11])  # IndexError: string index out of range

print(name[-1])  # output: a
print(name[-2])  # output: v  


print(name[2:5])  # output: han
print(name[0:5])  # output: Sahan
print(name[6:11])  # output: Silva


print(name[0:11:2])  # output: ShnSla
print(name[0:11:3])  # output: Sa ia

print(name[::-1])  # output: avliS nahS

print(name[:5]) # output: Sahan
print(name[0:5]) # output: Sahan

print(name[6:]) # output: Silva
print(name[6:11]) # output: Silva


# string concatenation
first_name = "Sahan"
last_name = "Silva"

full_name = first_name + " " + last_name
print(full_name)  # output: Sahan Silva

age = 25
info = full_name + " is " + str(age) + " years old."
print(info)  # output: Sahan Silva is 25 years old.
# TypeError: can only concatenate str (not "int") to str



# in and not in operators
message = "Hello, welcome to the world of Python programming."
print("welcome" in message)  # output: True
print("Java" in message)  # output: False

print("Python" not in message)  # output: False
print("Java" not in message)  # output: True

print("H" in message)  # output: True
print("h" in message)  # output: False (case-sensitive)





###################### String methods 1  ######################


    # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
text = "  Hello, World! Welcome to Python Programming.  "
print(text) # output:   Hello, World! Welcome to Python Programming.

print(text.lower()) # output:   hello, world! welcome to python programming.
print(text.upper()) # output:   HELLO, WORLD! WELCOME TO PYTHON PROGRAMMING.
print(text.strip()) # output: Hello, World! Welcome to Python Programming. 
print(text.title()) # output:   Hello, World! Welcome To Python Programming. # every word first letter is capitalized
print(text.capitalize()) # output:   Hello, world! welcome to python programming. # only first letter of the string is capitalized


print(text.replace("World", "Universe")) # output:   Hello, Universe! Welcome to Python Programming.
print(text.split(",")) # output: ['  Hello', ' World! Welcome to Python Programming.  ']
print(text.split()) # output: ['Hello,', 'World!', 'Welcome', 'to', 'Python', 'Programming.']


# find() - checking index in left to right

print(text.find("World")) # output: 9 - index of first occurrence in word "World"
print(text.find("Python")) # output: 27 - index of first occurrence in word "Python"

print(text.find("H")) # output: 2
print(text.find("J")) # output: -1 (not found)

print(text.find("W", 10)) # output: 16 (start searching from index 10)
print(text.find("o", 5, 20)) # output: 6 (searching between index 5 and 20)


print(text.find("P")) # checking index in left to right - output: 27


# rfind() - checking index in right to left
print(text.rfind("P")) # checking index in right to left - output: 34


# index() - checking index in left to right
print(text.index("World")) # output: 9 - index of first occurrence in word "World"

print (text.index("H")) # output: 2
# print(text.index("J")) # ValueError: substring not found

# difference between find() and index()
# find() returns -1 if the substring is not found
# index() raises a ValueError if the substring is not found

##############################################################################################


# count() - counts occurrences of a substring
#substring - sequence of characters in a string eg - "Welcome" in "Hello, World! Welcome to Python Programming. Welcome!"
print("count :",text.count("Welcome")) # output: count : 1
print("count",text.count("o")) # output: 6
print("count",text.count("P")) # output: 2

##############################################################################################


print(text.center(20)) # # output:   Hello, World! Welcome to Python Programming.  
print(text.center(50)) # output:           Hello, World! Welcome to Python Programming.

print(text.ljust(40)) # output:   Hello, World! Welcome to Python Programming.          - left aligned
print(text.rjust(40)) # output:         Hello, World! Welcome to Python Programming. - right aligned

print(text.center(10,"-")) # output: -------Hello, World! Welcome to Python Programming.-------
print(text.ljust(10,"-"))  # output:   Hello, World! Welcome to Python Programming.-----------------
print(text.rjust(10,"-")) # output: -----------------  Hello, World! Welcome to Python Programming.

text = "      Hello, World! Welcome to Python Programming.       "
print(text)
print(text.strip()) # output: Hello, World! Welcome to Python Programming. (leading and trailing spaces removed)
print(text.lstrip()) # output: Hello, World! Welcome to Python Programming. (leading spaces removed)
print(text.rstrip()) # output:       Hello, World! Welcome to Python Programming. (trailing spaces removed)

text = "---------- Hello, World! Welcome to Python Programming. ----------"
print(text.strip("-")) # output:  Hello, World! Welcome to Python Programming. (leading and trailing - removed)
print(text.lstrip("-")) # output:  Hello, World! Welcome to Python Programming. ---------- (leading - removed)
print(text.rstrip("-")) # output: ---------- Hello, World! Welcome to Python Programming. ---------- (trailing - removed)


###################### String methods 2  ######################
text = "Hello, World! Welcome to Python Programming. Welcome!"

# startwith()
print(text.startswith("H")) # output: True
print(text.startswith("e")) # output: False

print(text.startswith("Hello")) # output: True
print(text.startswith("Python")) # output: False
print(text.startswith("Welcome", 14)) # output: True (checking from index 14)



# endswith()
print(text.endswith("Welcome!")) # output: True
print(text.endswith("Hello")) # output: False
print(text.endswith("World!", 0, 13)) # output: True (checking between index 0 and 13)

print(text.endswith("e")) # output: False
print(text.endswith("!")) # output: True


#replace()
new_text = text.replace("Welcome", "Greetings")
print(new_text) # output: Hello, World! Greetings to Python Programming. Greetings!
new_text = text.replace(",", "----")
print(new_text) # output: Hello---- World! Welcome to Python Programming. Welcome!

#join()
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)
print(sentence) # output: Hello World from Python


x ="apple-banana-cherry"
y = "123"
print(x.join(y)) # output: 1apple-banana-cherry2apple-banana-cherry3

print(" ".join(y)) # output: 1 2 3
print("-".join(y)) # output: 1-2-3

# split()

fruits = "apple,banana,cherry,orange"
fruit_list = fruits.split(",")
print(fruit_list) # output: ['apple', 'banana', 'cherry', 'orange']

fruits = "apple,banana,cherry,orange\n 21 213 321 321"
fruit_list = fruits.splitlines() # split at line breaks
print(fruit_list) # output: ['apple,banana,cherry,orange', ' 21 213 321 321']
