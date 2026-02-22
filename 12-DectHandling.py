 ###################### Dictionary Data Type ######################

# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionaries are written with curly brackets {}.
# Dictionaries are mutable - we can change, add, remove items after the dictionary has been created. and when running the code.
# Dictionaries store data in key:value pairs.
my_dict = {
    "name": "Sahan Silva",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science", "History"]
}

print(my_dict) # output: {'name': 'Sahan Silva', 'age': 25, 'is_student': True, 'courses': ['Math', 'Science', 'History']}
print(type(my_dict)) # output: <class 'dict'>
print(len(my_dict)) # output: 4

print(my_dict["name"]) # output: Sahan Silva
print(my_dict.get("age")) # output: 25
print(my_dict["courses"][1]) # output: Science

# accessing keys and values
print(my_dict.keys()) # output: dict_keys(['name', 'age', 'is_student', 'courses'])
print(my_dict.values()) # output: dict_values(['Sahan Silva', 25, True, ['Math', 'Science', 'History']])
print(my_dict.items()) # output: dict_items([('name', 'Sahan Silva'), ('age', 25), ('is_student', True), ('courses', ['Math', 'Science', 'History'])])

# adding items
my_dict["grade"] = "A"
print(my_dict) # output: {'name': 'Sahan Silva', 'age': 25, 'is_student': True, 'courses': ['Math', 'Science', 'History'], 'grade': 'A'}

# updating items or modifying items
my_dict["age"] = 26
print(my_dict) # output: {'name': 'Sahan Silva', 'age': 26, 'is_student': True, 'courses': ['Math', 'Science', 'History'], 'grade': 'A'}

# removing items
# my_dict.pop("is_student")
print(my_dict.pop("is_student"))  # output: True - value of the removed key displayed and removes the key-value pair

print(my_dict) # output: {'name': 'Sahan Silva', 'age': 26, 'courses': ['Math', 'Science', 'History'], 'grade': 'A'}


print(my_dict.popitem()) # output: ('grade', 'A') and removes the last inserted item


del my_dict["grade"]
print(my_dict) # output: {'name': 'Sahan Silva', 'age': 26, 'courses': ['Math', 'Science', 'History']}

my_dict.clear() # removes all items
print(my_dict) # output: {}

# del my_dict # deletes the dictionary completely
# print(my_dict) # raises an error because the dictionary no longer exists


# adding multiple items at once
my_dict = {}
my_dict.update({
    "name": "Sahan Silva",
    "age": 25,
    "is_student": True
})
print(my_dict) # output: {'name': 'Sahan Silva', 'age': 25, 'is_student': True}



# looping through dictionary

my_dict = {
    "name": "Sahan Silva",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science", "History"]
}

for key in my_dict:
    print(key) # output: name age is_student courses
    
for key, value in my_dict.items():
    print(f"{key}: {value}")
    # output:
    # name: Sahan Silva
    # age: 25
    # is_student: True
    # courses: ['Math', 'Science', 'History']

# dictionary methods
print(my_dict.copy()) # output: {'name': 'Sahan Silva', 'age': 25, 'is_student': True, 'courses': ['Math', 'Science', 'History']}
print(my_dict.get("name")) # output: Sahan Silva
print(my_dict.popitem()) # output: ('courses', ['Math', 'Science', 'History'])
print(my_dict) # output: {'name': 'Sahan Silva', 'age': 25, 'is_student': True}
