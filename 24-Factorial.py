################### Factorial of a Number ###################

# n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1

# 4! = 4 × 3 × 2 × 1 = 24

for i in range(1, 6):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print(f"Factorial of {i} is {factorial}")


userinput = input("Enter a number to calculate its factorial: ")
if userinput.isdigit():
    x = int(userinput)
    result = 1
    for i in range(1, x + 1):
        result *= i
        print(f"Factorial of {x} is {result}")

        # or



userinput = int(input("Enter a number to calculate its factorial: "))
x = userinput
result = 1
for i in range(1, x + 1):
    result *= i
    print(f"Factorial of {x} is {result}") 