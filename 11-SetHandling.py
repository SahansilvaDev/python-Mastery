 ###################### Set Data Type ######################

# Sets is a collection which is unordered and unindexed. No duplicate members. and we can not use indexing or slicing to access items. because its unordered.
# Sets are written with curly brackets {}.
# Sets is mutable - we can change, add, remove items after the set has been created. and when running the code.

my_set = {"apple", "banana", "cherry"}
print(my_set) # output: {'banana', 'cherry', 'apple'} (order may vary)
my_set2 = set(("apple", "banana", "cherry"))
print(my_set2) # output: {'banana', 'cherry', 'apple'} (order may vary)
print(type(my_set)) # output: <class 'set'>
print(len(my_set)) # output: 3
# we cannot access items in a set by referring to an index or a key.
# But we can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for item in my_set:
    print(item) # output: banana cherry apple (order may vary)

print("banana" in my_set) # output: True
print("orange" in my_set) # output: False

# Adding items
my_set.add("orange")
print(my_set) # output: {'banana', 'cherry', 'apple', 'orange'} (order may vary)

my_set.update(["mango", "grape"])
print(my_set) # output: {'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'} (order may vary)
# we can add different data types in a set
my_set.update([1, 2.5, True])
print(my_set) # output: {1, 2.5, True, 'banana', 'cherry', 'apple', 'orange', 'mango', 'grape'} (order may vary)

# Removing items
my_set.remove("banana") # raises an error if item not found
print(my_set) # output: {1, 2.5, True, 'cherry', 'apple', 'orange', 'mango', 'grape'} (order may vary)

my_set.discard("cherry") # does not raise an error if item not found
print(my_set) # output: {1, 2.5, True, 'apple', 'orange', 'mango', 'grape'} (order may vary)

my_set.pop() # removes and returns an arbitrary item
print(my_set) # output: {2.5, True, 'apple', 'orange', 'mango', 'grape'} (order may vary)

my_set.clear() # removes all items
print(my_set) # output: set()

# del my_set # deletes the set completely
# print(my_set) # raises an error because the set no longer exists

# set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union
set_union = set_a.union(set_b)
print(set_union) # output: {1, 2, 3, 4, 5, 6}

# intersection
set_intersection = set_a.intersection(set_b)
print(set_intersection) # output: {3, 4}

# difference
set_difference = set_a.difference(set_b)
print(set_difference) # output: {1, 2}

# symmetric difference
set_sym_diff = set_a.symmetric_difference(set_b) # items in either set_a or set_b but not in both
print(set_sym_diff) # output: {1, 2, 5, 6}

# subset and superset
set_c = {1, 2}
print(set_c.issubset(set_a)) # output: True
print(set_a.issuperset(set_c)) # output: True

# disjoint
set_d = {5, 6}
print(set_a.isdisjoint(set_d)) # output: True
set_e = {4, 5}
print(set_a.isdisjoint(set_e)) # output: False

# copying sets
set_f = set_a.copy()
print(set_f) # output: {1, 2, 3, 4}
