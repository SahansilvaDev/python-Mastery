n=5

for i in range(n):
    for j in range(i + 1):
        print("*", end="") # this will print * without a new line after each iteration of the inner loop
    print() # this will print a new line after each iteration of the outer loop




'''

*
**
***
****
*****


'''

m=5

for i in range(m):
    for j in range(m-i):
        print("*", end="") # this will print * without a new line after each iteration of the inner loop
    print() # this will print a new line after each iteration of the outer loop

'''

*****
****
***
**
*

'''

m=5

for i in range(m):
    for j in range(m-i-1):
        print(" ", end="") # this will print * without a new line after each iteration of the inner loop

    for k in range(2*i+1):
        print("*", end="") # this will print space without a new line after each iteration of the inner loop
    print() # this will print a new line after each iteration of the outer loop


'''

    *
   ***
  *****
 *******
*********

'''

# heart shape

for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
 ** **
*  *  *
*     *
 *   *
  * *
   *

'''