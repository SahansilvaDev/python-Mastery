# File Handling - OS Module in Python
# The os module in Python provides a way of using operating system dependent functionality 
# like reading or writing to the file system.
# It allows you to interact with the underlying operating system in a platform-independent way.


'''
read(): This method is used to read the entire content of a file.
write(): This method is used to write data to a file.
remove(): This method is used to delete a file from the file system.
mkdir(): This method is used to create a new directory.
listdir(): This method is used to list all files and directories in a specified directory.

'r' - Read mode: This mode is used to read the contents of a file. The file pointer is placed at the beginning of the file.
'w' - Write mode: This mode is used to write data to a file. If the file already exists, its contents are truncated. If the file does not exist, a new file is created.
'a' - Append mode: This mode is used to append data to the end of a file. If the file does not exist, a new file is created.
'w+' - Write and Read mode: This mode is used to write and read data to/from a file. If the file already exists, its contents are truncated. If the file does not exist, a new file is created.

'''


r'''

x = open('test.txt', 'r') # opening the file in read mode
The error occurs because your script is trying to open 'test.txt' in read mode 
from the current working directory, which is likely d:\Coding learning\Python\python-Mastery, 
not the 37-FileHandling subfolder where test.txt actually exists.

# Tip:Always check your script's working directory with:

import os
print(os.getcwd()) # getting the current working directory
This helps you understand where Python is looking for files.


'''

# correct relative path
x = open('37-FileHandling/test.txt', 'r') # opening the file in read mode
#or absolute path
# x = open(r'd:\Coding learning\Python\python-Mastery\37-FileHandling\test.txt', 'r')


print(x.read()) # reading the content of the file , if use readlines() method it will return a first line in the file
x.close() # closing the file after reading

# when always close file  read or write to it, otherwise 
# it will cause memory leak and it will also cause data loss 
# if we are writing to the file and we forget to close the file after writing to it.

# to prevent always .close() method using

with open('37-FileHandling/test.txt', 'r') as x: # opening the file in read mode using with statement
    print(x.read()) # reading the content of the file
# with statement will automatically close the file after the block of code is executed,
# even if an exception occurs, it will still close the file properly.

# output:
# this is from test.txt file




# x = open('test.txt', 'w') # creating a new file in write mode
# x.write("Hello, this is from python script file write method") # writing data to the file
# x.close() # closing the file after writing to it

with open('37-FileHandling/test.txt', 'w') as x: # opening the file in write mode using with statement
    x.write("Hello, this is from python script file write method") # writing data to the file
# with statement will automatically close the file after the block of code is executed,
# even if an exception occurs, it will still close the file properly.
# and now remove all content in the file and write new content to the file



with open('37-FileHandling/test.txt', 'r') as x:
    print(x.read()) # output: Hello, this is from python script file write method



# fo if need write without removing the content in the file then 
# we can use append mode 'a' instead of write mode 'w'

with open('37-FileHandling/test.txt', 'a') as x: # opening the file in append mode using with statement
    x.write("\nthis to test.txt using append mode") # writing data to the file


with open('37-FileHandling/test.txt', 'r') as x:
    print(x.read()) 
    # output: 
    # Hello, this is from python script file write method 
    # this to test.txt using append mode








# The warning is caused by the string  '''   containing backslashes (like \C) inside your docstring or comment block.
# Python interprets backslashes as escape characters unless you use a raw string.

# How to fix:
# If your docstring or comment contains Windows paths, use a raw string or double backslashes:

# r'''
# Example: d:\\Coding learning\\Python\\python-Mastery\\37-FileHandling\\test.txt
# '''
# Or escape the backslashes:
# '''
# Example: d:\\Coding learning\\Python\\python-Mastery\\37-FileHandling\\test.txt
# '''
# This will remove the SyntaxWarning.



print("######################  Image open  ######################")

x = open('37-FileHandling/image.png', 'rb') # opening the image file in binary read mode
# 'rb' mode is used to read binary files like images, videos, etc.


print(x.read()) # reading the content of the image file in binary format
x.close() # closing the file after reading








###################### os module  ######################

import os

print(os.getcwd()) # getting the current working directory
# os module provides a way of using operating system dependent functionality like reading or writing to the file system.
# it allows you to interact with the underlying operating system in a platform-independent way.

os.remove('hello.txt') # removing a file from the file system
os.mkdir('new_folder') # creating a new directory
print(os.listdir()) # listing all files and directories in the current directory

os.rename('old_name.txt', 'new_name.txt') # renaming a file from old_name.txt to new_name.txt

os.path.exists('test.txt') # checking if a file exists in the file system, it will return True if the file exists and False if the file does not exist
print(os.path.exists('test.txt')) # output: True
print(os.path.exists('non_existent_file.txt')) # output: False

print(os.path.abspath('test.txt')) 
print(os.path.getsize('test.txt')) 




os.chdir('37-FileHandling') # changing the current working directory to 37-FileHandling
#or 
os.chdir(r'd:\Coding learning\Python\python-Mastery\37-FileHandling') # changing the current working directory to 37-FileHandling

print(os.getcwd()) # output: d:\Coding learning\Python\python-Mastery\37-FileHandling


print(os.listdir()) # output: ['image.png', 'test.txt'] because we changed the current working directory to 37-FileHandling and 
# now we are listing all files and directories in the current working directory which is 37-FileHandling 
# and it contains image.png and test.txt files

os.mkdir('new_folder') # creating a new directory in the current working directory which is 37-FileHandling
print(os.listdir()) # output: ['image.png', 'new_folder', 'test.txt']

os.mkdir('new_folder/new') # creating a new directory in the current working directory which is 37-FileHandling
print(os.listdir()) # output: ['image.png', 'new_folder', 'test.txt']



os.rmdir('new_folder/new') # removing a directory from the file system
print(os.listdir()) # output: ['image.png', 'new_folder', 'test.txt']

os.rename('new_folder', 'renamed_folder') # renaming a directory from new_folder to renamed_folder
print(os.listdir()) # output: ['image.png', 'renamed_folder', 'test.txt']

print(os.path.exists('new_folder')) # checking if the new_folder directory exists in the file system, it will return False because we renamed it to renamed_folder
print(os.path.exists('renamed_folder')) # checking if the renamed_folder directory exists in the

print(dir(os)) # printing all the functions and variables in the os module
print(len(dir(os))) # output: 153 because there are 153 functions and variables in the os module


print(help(os)) # printing the documentation of the os module
print(help(os.listdir)) # printing the documentation of the listdir function in the os module

print("######################  End of File Handling - OS Module  ######################")