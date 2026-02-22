import random
x = random.random() # generating a random float number between 0 and 1
print(x) # output: a random float number between 0 and 1

x = random.random()*100
print(x) # output: a random float number between 0 and 100


x = random.uniform(0, 10) # generating a random float number between 0 and 10
print(x) # output: a random float number between 0 and 10


y = random.randint(1, 10) # generating a random integer between 1 and 10
print(y) # output: a random integer between 1 and 10

z = random.choice(['apple', 'banana', 'orange']) # randomly selecting an element from a list
print(z) # output: a random element from the list ['apple', 'banana', 'orange']

names = ['Alice', 'Bob', 'Charlie', 'David']
winner = random.choices(names, k=2) # randomly selecting an element from the names list
print(winner) # output: a random name from the names list

numbers =list(range(1, 11)) # creating a list of numbers from 1 to 10
random.shuffle(numbers) # shuffling the numbers list in place
print(numbers) # output: a shuffled list of numbers from 1 to 10