# List vs Array

# List we can store different data types
my_list = [1, "Hello", 3.14, True]

# Array we can store only same data type
import array
array_of_int = [1, 2, 3, 4]
my_array = array.array('i', [1, 2, 3, 4]) # 'i' is the type code for integer 

'''
Data type code for array:

Type code	Description
'b'	signed char
'B'	unsigned char
'u'	Py_UNICODE character
'h'	signed short
'H'	unsigned short
'i'	signed int
'I'	unsigned int
'l'	signed long
'L'	unsigned long
'q'	signed long long
'Q'	unsigned long long
'f'	float
'd'	double
's'	char[] (string)
'm'	Py_ssize_t (used for array length)

'''


import array    

x =array.array('i', [1, 2, -3, 4]) # creating an array of integers (can store both positive and negative integers)
y =array.array('I', [1, 2, 3, 4]) # creating an array of unsigned integers  (only can store positive integers)

print(x) # output: array('i', [1, 2, -3, 4])
print(y) # output: array('I', [1, 2, 3, 4])

print(x[0]) # output: 1
print(x[1:3]) # output: array('i', [2, -3])


array.array('f', [1.0, 2.0, 3.0, 4.0]) # creating an array of floats




from array import * # call all functions from array module without using array. prefix

x =array('i', [1, 2, -3, 4]) 
print(x) # output: array('i', [1, 2, -3, 4])
print(x[0]) # output: 1

x.append(5) # adding an element to the end of the array
print(x) # output: array('i', [1, 2, -3, 4, 5])

x.insert(2, 10) # inserting an element at a specific index
print(x) # output: array('i', [1, 2, 10, -3, 4, 5])

x.remove(10) # removing an element from the array
print(x) # output: array('i', [1, 2, -3, 4, 5])

x.pop() # removing the last element from the array
print(x) # output: array('i', [1, 2, -3, 4])

x.pop(1) # removing an element at a specific index
print(x) # output: array('i', [1, -3, 4])

x.extend([6, 7, 8]) # adding multiple elements to the end of the array
print(x) # output: array('i', [1, -3, 4, 6, 7, 8])

x.reverse() # reversing the array
print(x) # output: array('i', [8, 7, 6, 4, -3, 1])



x =array('i', [1, 2, -3, 4])  
y =array('i', [1, 2, 3, 4])
z=x+y # adding two arrays of the same data type need i type and other also need simple i 
print(z) # output: array('i', [1, 2, -3, 4, 1, 2, 3, 4])


for i in range(len(x)):
    print(x[i]) # output: 1, 2, -3, 4

for i in x:
    print(i) # output: 1, 2, -3, 4