# Arithmatic Operators - +, -, *, /, %, **, //
# Assignment Operators - =, +=, -=, *=, /=, %=, **=, //=
# Comparison Operators - ==, !=, >, <, >=, <=
# Logical Operators - and, or, not
# Identity Operators - is, is not
# Membership Operators - in, not in
# Bitwise Operators - &, |, ^, ~, <<, >>


############################################# Arithmatic Operators #############################################
# +, -, *, /, %, **, //


# Addition
a = 10  
b = 20
c = a + b
print(c)

# Subtraction
c = a - b
print(c)

# Multiplication
c = a * b

# Division
c = a / b


# Exponentiation ** - power
c = a ** b # 10 ** 20 = 100000000000000000000
# eg 11 ** 3 = 11 * 11 * 11 = 1331

# Modulus % - remainder
c = a % b # 10 % 20 = 10 - 0 times 20 is 0 and 10 is the remainder (5 % 2 = 1)
print(c)



# Floor Division // - quotient
c = a // b  
# e g 5 // 2 = 2 
a = 5
b = 2
c = a // b

print(c) # 2

c = 5 /2

print(c) # 2.5


#######  Operator Precedence  ########

#     ()            - Parentheses
#     **            - Exponentiation
#    * / % //       - Multiplication, Division, Modulus, Floor Division
#    + -            - Addition, Subtraction



############################################# Assignment Operators #############################################

# =, +=, -=, *=, /=, %=, **=, //=


a = 10
b = 20

# +=
a += b # a = a + b
print(a) # 30


a = 10
b = 20


# -=
a -= b # a = a - b
print(a) # -10


a = 10
b = 20



# *=
a *= b # a = a * b
print(a) # 200

# /=
a = 10
b = 20
a /= b # a = a / b
print(a) # 0.5

# %=
a = 10
b = 20
a %= b # a = a % b
print(a) # 10


# **=
a = 10
b = 20
a **= b # a = a ** b
print(a) # 100000000000000000000

# //=
a = 5
b = 2
a //= b # a = a // b
print(a) # 2



############################################# Comparison Operators #############################################

'''
== - Equal
!= - Not Equal
> - Greater than
< - Less than
>= - Greater than or Equal to
<= - Less than or Equal to

'''


a = 10
b = 20

# ==
c = a == b
print(c) # False

# !=
c = a != b
print(c) # True

# >
c = a > b
print(c) # False

# <
c = a < b
print(c) # True

# >=
c = a >= b
print(c) # False

# <=
c = a <= b
print(c) # True





############################################# Logical Operators #############################################

'''
and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverse the result, returns False if the result is true

'''

a = 10
b = 20

# and
c = a > 5 and b < 30
print(c) # True

# or
c = a > 5 or b < 30
print(c) # True

# not
c = not(a > 5 and b < 30)
print(c) # False




############################################# Identity Operators #############################################

# is, is not - checking if they are same memory location or not

a = 10
b = 10
z = 20

print(id(a))
print(id(b))
print(id(z))

c = a is b
print(c) # True

c = a is not b
print(c) # False

c = a is z
print(c) # False



############################################# Membership Operators #############################################

a = [1, 2, 3, 4, 5]

# in
c = 1 in a
print(c) # True

# not in
c = 1 not in a
print(c) # False





############################################# Bitwise Operators #############################################

'''
& - AND
| - OR
^ - XOR
~ - NOT
<< - Left Shift
>> - Right Shift

'''

a = 10
b = 20

# &
c = a & b
print(c) # 0

# |
c = a | b
print(c) # 30

# ^
c = a ^ b
print(c) # 30

# ~
c = ~a
print(c) # -11

# << - Left Shift
c = a << 1
print(c) # 20

# >> - Right Shift
c = a >> 1
print(c) # 5