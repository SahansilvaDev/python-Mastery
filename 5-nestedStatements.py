
# Nested if else Statements

number = 6

if number > 0:
    print("Positive")
else:
    if number < 0:
        print("Negative")
    else:
        print("Zero")


if number != 0:
    if  number > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")
    