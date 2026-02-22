# zip function is used to combine lists, tuples, set, dictionary or any iterable objects into a single iterable object. 
# It takes multiple iterables as arguments and returns an iterator of tuples, 
# where the i-th tuple contains the i-th element from each of the input iterables. 
# The returned iterator stops when the shortest input iterable is exhausted.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2) # creating a zip object from the two lists
print(list(zipped)) # output: [(1, 'a'), (2, 'b'), (3, 'c')], because the zip function combines the two lists into a list of tuples
print(tuple(zipped)) # output: ((1, 'a'), (2, 'b'), (3, 'c')), because the zip function combines the two lists into a list of tuples
print(set(zipped)) # output: {(1, 'a'), (2, 'b'), (3, 'c')}, because the zip function combines the two lists into a list of tuples
print(dict(zipped)) # output: {1: 'a', 2: 'b', 3: 'c'}, because the zip function combines the two lists into a list of tuples

# or
zipped = zip(list1, list2) # creating a zip object from the two lists
for item in zipped:
    print(item) # output: (1, 'a'), (2, 'b'), (3, 'c'), because the zip function combines the two lists into a list of tuples and 
    # we are iterating through the zip object to print each tuple



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
zipped = zip(list1, list2, list3) # creating a zip object from the three lists
print(list(zipped)) # output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)], 
# because the zip function combines the three lists into a list of tuples

unzipped = zip(*zipped) # unzipping the zipped object using the * operator
print(list(unzipped)) # output: [(1, 2, 3), ('a', 'b', 'c'), (True, False, True)], 
#because the * operator is used to unpack the zipped object and create a new zip object with the original lists as tuples.
