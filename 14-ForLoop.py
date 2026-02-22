x = [1,2,3,4,5]

print(5 in x)  # output: True


for item in x:
    print("Item:", item)
# output:
# Item: 1
# Item: 2
# Item: 3
# Item: 4
# Item: 5


for num in x:
    print("Number in List:", num)
# output:
# Number in List: 1
# Number in List: 2
# Number in List: 3
# Number in List: 4
# Number in List: 5



x = {'name': 'Sahan', 'age': 30, 'city': 'Colombo'}

for value in x.values():
    print("Value:", value)
# output:
# Value: Sahan
# Value: 30
# Value: Colombo


for key in x.keys():
    print("Key:", key)
# output:
# Key: name
# Key: age
# Key: city

for key in x:
    print("Key:", key)
# output:
# Key: name
# Key: age
# Key: city

for key in x:
    print("Key:", key, "Value:", x[key])
# output:
# Key: name Value: Sahan
# Key: age Value: 30
# Key: city Value: Colombo

for key, value in x.items():
    print("Key:", key, "Value:", value)

# output:
# Key: name Value: Sahan
# Key: age Value: 30
# Key: city Value: Colombo

for i,j in x.items():
    print("Key:", i, "Value:", j)
# output:
# Key: name Value: Sahan
# Key: age Value: 30
# Key: city Value: Colombo

for i in x.items():
    print(i)
# output:
# ('name', 'Sahan')
# ('age', 30)
# ('city', 'Colombo')



for i in range(5):
    print("Iteration:", i)
# output:
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

for i in range(1, 6):
    print("Iteration:", i)
# output:
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4
# Iteration: 5

for i in range(0, 11, 2):
    print("Iteration:", i)
# output:
# Iteration: 0
# Iteration: 2
# Iteration: 4
# Iteration: 6
# Iteration: 8
# Iteration: 10

