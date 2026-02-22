# n! = n* (n-1)! for n > 0
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# how this works:
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 * factorial(0)
# factorial(0) = 1



print(factorial(5))  # output: 120


# for i in range(1, 6):
#     print(f"Factorial of {i} is {factorial(i)}")
