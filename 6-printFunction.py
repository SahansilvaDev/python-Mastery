# Escaape Sequences
'''
\n - New Line character
\r - Carriage Return - moves the cursor to the beginning of the line
\t - Tab
\b - Backspace - deletes the character


'''


print("Hello\nWorld") 

print("Hellow\rWorld") # Output: Worldw (Carriage return moves the cursor to the beginning of the line, overwriting "Hellow" with "Worldw")


print("Hello\tWorld")

print("Hello\bWorld") # Output: HellWorld



# Print Function

name = "John"
age = 23
score = 98.5

print(name)
print(name,end="\n") 
print(age,end="\n") 
print(score,end="\n") 

# output
'''
john
23
98.5

'''

print(name,end="")
print(age,end="") 
print(score,end="") 

# output
'''
john2398.5

'''

print(name,end="-")
print(age,end="-") 
print(score,end="-") 

# output
'''
john-23-98.5-

'''

print(name, age, score) # Output: John 23 98.5
print(name, age, score, sep=", ") # Output: John, 23, 98.5
print(name, age, score, sep=" | ") # Output: John | 23 | 98.5



print("Name: ", name, "Age: ", age, "Score: ", score) # Output: Name: John Age: 23 Score: 98.5


################################### Formatted Printing ########################################

name , age , score = "John", 23, 98.5

# He is John, He is 23 years old and he scored 98.5 marks

''' print("He is "+name+". He is "+age+" years old and he scored "+score+" marks") '''

# Error: TypeError: can only concatenate str (not "int") to str



# There are 3 ways to solve this problem


# Method 01

print("He is "+name+". He is "+str(age)+" years old and he scored "+str(score)+" marks") # Output: He is John. He is 23 years old and he scored 98.5 marks

# Method 02

print("He is %s. He is %d years old and he scored %.2f marks" %(name, age, score)) # Output: He is John. He is 23 years old and he scored 98.500000 marks

# Method 03

print("He is {}. He is {} years old and he scored {} marks" .format(name, age, score)) # Output: He is John. He is 23 years old and he scored 98.5 marks



print("He is {0}. He is {2} years old and he scored {1} marks" .format(name, score, age)) 

##########  New Method  ############

print(f"He is {name}. He is {age} years old and he scored {score} marks") # Output: He is John. He is 23 years old and he scored 98.5 marks

 