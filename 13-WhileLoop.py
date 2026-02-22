# while(condition):


i = 0
while(i<5):
    print("Iteration:", i)
    i += 1

#output:
# iteration: 0
# iteration: 1
# iteration: 2
# iteration: 3
#iteration: 4




i = 0
while(i<=10):
    print("Iteration:", i)
    i += 1





user_input = input("Enter number then iterate till that number: ")
if user_input.isdigit():
    num = int(user_input)
    i = 1
    sum = 0
    while i <= num:
        print(f"Sum of value {sum},Iteration: {i}")
        i,sum = i + 1, sum + i
    print("Final Sum:", sum)

else:
    print("Please enter a valid number.")




while True:
    user_input = input("Enter 'exit' to quit the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")

