lst = [1,2,3,4,5]

for i in lst:
    print(i) # output: 1, 2, 3, 4, 5


print(lst[0])

set ={1,2,3,4,5}

itr = iter(set) # creating an iterator object from the set
print(next(itr)) # output: 1
print(next(itr)) # output: 2    




itr = iter(set) # creating an iterator object from the set
while True:
    try:
        print(next(itr)) # output: 1, 2, 3, 4, 5
    except StopIteration:
        break # when there are no more elements to iterate, it will raise StopIteration exception and we can break the loop



####### creating our own iterator class ##############

class myit:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


myobj = myit([1, 2, 3, 4, 5]) # creating an object of myit class with a list of data
itr = iter(myobj) # creating an iterator object from the myit class
print(next(itr)) # output: 1
print(next(itr)) # output: 2
print(next(itr)) # output: 3
print(next(itr)) # output: 4
print(next(itr)) # output: 5
# when we try to call next() after the last element, it will raise StopIteration exception and we can handle it using try-except block

'''
In Python, methods like __init__, __iter__, and __next__ are called special methods or dunder methods 
(short for "double underscore").
They are used to give objects special behavior, such as making them iterable or 
defining how they are initialized.


__init__: Called when you create a new object. It initializes the object's attributes.
__iter__: Makes the object iterable (so you can use it in a for loop).
__next__: Returns the next item from the iterator. Raises StopIteration when there are no more items.

The double underscores (__) are used to avoid naming conflicts with user-defined methods and to 
signal that these methods have special meaning in Python's language features.


'''




