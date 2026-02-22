'''
Regular expressions are a powerful tool for matching patterns in strings. 
They are used for searching, replacing, and validating strings based on specific patterns. 
In Python, the 're' module provides functions for working with regular expressions.

Regular expression patterns are defined using a special syntax that 
includes various characters and symbols to represent different types of matches.

For example, the pattern '\d' matches any digit, 
while the pattern '\w' matches any word character (letters, digits, and underscores).

Regular expressions can be used for a wide range of applications, such as validating email addresses, 
extracting phone numbers from text, and performing complex search-and-replace operations on strings.

'''

# meta characters in regular expressions
# . ^ $ * + ? { } [ ] \ | ( )
# . matches any character except a newline.
# ^ matches the start of the string.
# $ matches the end of the string.
# * matches 0 or more occurrences of the preceding element.
# + matches 1 or more occurrences of the preceding element.
# ? matches 0 or 1 occurrence of the preceding element.
# { } matches a specific number of occurrences of the preceding element.
# [ ] matches any character within the brackets.
# \ escapes a special character.
# | acts as an OR operator.
# ( ) groups patterns together.

# symbols description example
# \d matches any digit character   '0'-'9'
# \w matches any word character    'a'-'z', 'A'-'Z', '0'-'9', '_'
# \W matches any non-word character    '.', ' ', '!', '@', '#', etc.
# \s matches any whitespace character   ' ', '\t', '\n', '\r', '\f', '\v'
# \S matches any non-whitespace character   'a', '1', '_', 'A','@'

import re

string = "The price of the product is $100. Contact us at info@example.com."
y = re.findall(r'\$\d+', string) # find all occurrences of a pattern that matches a dollar sign followed by one or more digits
print(y) # output: ['$100']

y = re.findall(r'\w+@\w+\.\w+', string) # find all occurrences of a pattern that matches an email address
print(y) # output: ['info@example.com']

y = re.findall(r'\d', string) # find all occurrences of a pattern that matches a digit
print(y) # output: ['1', '0', '0']

y = re.findall(r'.', string) # find all occurrences of a pattern that matches any character except a newline
print(y) # output: ['T', 'h', 'e', ' ', 'p', 'r', 'i', 'c', 'e', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'p', 'r', 'o', 'd', 'u', 'c', 't', ' ', 'i', 's', ' ', '$', '1', '0', '0', '.', ' ', 'C', 'o', 'n', 't', 'a', 'c', 't', ' ', 'u', 's', ' ', 'a', 't', ' ', 'i', 'n', 'f', 'o', '@', 'e', 'x', 'a', 'm', 'p', 'l', 'e', '.', 'c', 'o', 'm', '.']


y = re.findall(r'\w\w\w', string) # find all occurrences of a pattern that matches three word characters in a row
print(y) # output:  ['The', 'pri', 'the', 'pro', 'duc', '100', 'Con', 'tac', 'inf', 'exa', 'mpl', 'com']


y = re.findall(r'\W\w\w\w\W', string) 
print(y) # output:  [' the ', '$100.', '.com.'] 

y = re.findall(r'\w{3}', string) 
print(y) # output:  ['The', 'pri', 'the', 'pro', 'duc', '100', 'Con', 'tac', 'inf', 'exa', 'mpl', 'com'] 

y = re.findall(r'\w{4,6}', string) 
print(y) # output: ['price', 'produc', 'Contac', 'info', 'exampl']

y = re.findall(r'\w+', string) 
print(y) # output: ['The', 'price', 'of', 'the', 'product', 'is', '100', 'Contact', 'us', 'at', 'info', 'example', 'com']

y = re.findall(r'\w*', string) 
print(y) # output: ['The', '', 'price', '', 'of', '', 'the', '', 'product', '', 'is', '', '', '100', '', '', 'Contact', '', 'us', '', 'at', '', 'info', '', 'example', '', 'com', '', '']


y = re.findall(r'\w?', string) 
print(y) # output: ['T', 'h', 'e', '', 'p', 'r', 'i', 'c', 'e', '', 'o', 'f', '', 't', 'h', 'e', '', 'p', 'r', 'o', 'd', 'u', 'c', 't', '', 'i', 's', '', '', '1', '0', '0', '', '', 'C', 'o', 'n', 't', 'a', 'c', 't', '', 'u', 's', '', 'a', 't', '', 'i', 'n', 'f', 'o', '', 'e', 'x', 'a', 'm', 'p', 'l', 'e', '', 'c', 'o', 'm', '', '']      


y = re.findall(r'^\w+', string) 
print(y) # output: ['The']  # find the first word at the beginning of the string

y = re.findall(r'\w+$', string) 
print(y) # output: []  # find the last word at the end of the string , this not showing the last word because of the dot at the end of the string, so we need to remove the dot from the string to get the last word

string2 = "Helloo world"
y = re.findall(r'\w+$', string2) 
print(y) # output: ['world']  # find the last word at the end of the string


# finall() function returns a list of all matches found in the string, 
# while search() function returns a match object for the first match found in the string. If no match is found, search() returns None.
# split() function splits the string into a list of substrings based on a specified pattern, 
# while sub() function replaces occurrences of a pattern in the string with a specified replacement string.

string = "The price of the product is $100. Contact us at info@gmail.com."



y = re.findall(r'\w+@gmail.com', string) # find all occurrences of a pattern that matches a gmail email address
print(y) # output: ['info@example.com']



y = re.findall(r'T\w+', string) # find all occurrences of a pattern that matches a T and after that any word characters
print(y) # output: ['The']


y = re.findall(r'\w*a\w+', string) # find all occurrences of a pattern that matches any word containing the letter 'a'
print(y) # output: ['Contact', 'at', 'gmail']


y = re.search(r'\w+', string)
print(y) # output: <re.Match object; span=(0, 6), match='The'>  # find the first word in the string

y = re.search(r'\w+@gmail.com', string)
print(y) # output: <re.Match object; span=(48, 62), match='info@gmail.com'>


y = re.split(r'\s', string) # split the string into a list of words based on whitespace
print(y) # output: ['The', 'price', 'of', 'the', 'product', 'is', '$100.', 'Contact', 'us', 'at', 'info@gmail.com.']


y = re.split(r'\s', string) # split the string into a list of words based on whitespace
print(y) # output: ['The', 'price', 'of', 'the', 'product', 'is', '$100.', 'Contact', 'us', 'at', 'info@gmail.com.']


y = re.split(r'\s', string, 4) # split the string into a list of words based on whitespace
print(y) # output: ['The', 'price', 'of', 'the', 'product is $100. Contact us at info@gmail.com.']


y = re.sub(r'\s', '@', string) # replace all whitespace characters with the string
print(y) # output: The@price@of@the@product@is@$100.@Contact@us@at@info@gmail.com.

y = re.sub(r'\s', '@', string, 4) # replace the first 4 whitespace characters with the string
print(y) # output: The@price@of@the@product is $100. Contact us at info@gmail.com.

y = re.sub(r'i\w{3}', 'hello', string) # replace all whitespace characters with the string
print(y) # output: The price of the product is $100. Contact us at hello@gmail.com.
