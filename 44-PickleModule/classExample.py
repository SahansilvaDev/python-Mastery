import pickle

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")

person1 = Person("kamal", 20, 56.2)
person2 = Person("sara", 22, 52.5)

# wb - write binary mode
with open('44-PickleModule/persons.pkl', 'wb') as f:
    pickle.dump(person1, f)
    pickle.dump(person2, f)

# rb - read binary mode - loading the data back
with open('44-PickleModule/persons.pkl', 'rb') as f:
    loaded_person1 = pickle.load(f)
    loaded_person2 = pickle.load(f)
    

    print("Loaded Person 1:")
    loaded_person1.display_info()

    print(loaded_person1.name)  # output: kamal
    print(loaded_person1.age)   # output: 20
    print(loaded_person1.weight) # output: 56.2

    print(loaded_person2.name)  # output: sara
    print(loaded_person2.age)   # output: 22
    print(loaded_person2.weight) # output: 52.5