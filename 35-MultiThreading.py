def func1():
    for i in range(5):
        print("Function 1")

def func2():
    for i in range(5):
        print("Function 2")

func1() # calling func1 # this will execute func1 first and then func2 and this will not run simultaneously
func2() # calling func2 # these two functions write in main thread and they will execute sequentially, not simultaneously
# output:
# Function 1
# Function 1
# Function 1
# Function 1
# Function 1
# Function 2
# Function 2
# Function 2
# Function 2
# Function 2

''' 
when we call func1 and func2 sequentially, they will execute one after the other,
but if we want to execute them simultaneously, we can use threading module in Python.
this func1 and func2 will run in separate threads, allowing them to execute concurrently.
'''

############# Threading in Python ##############

print("Threading in Python")

import threading
from time import sleep

print("Using functions to create threads working with threading module in simultaneously")

#using threading module to run func1 and func2 simultaneously 
def func1():
    for i in range(5):
        print("Function 1")
        sleep(1) # adding a delay of 1 second to simulate some work being done

def func2():
    for i in range(5):
        print("Function 2")
        sleep(1) # adding a delay of 1 second to simulate some work being done





t1 = threading.Thread(target=func1) # creating a thread for func1
t2 = threading.Thread(target=func2) # creating a thread for func2
t1.start() # starting the thread for func1
sleep(0.1) # adding a small delay to ensure that func1 starts before func2
t2.start() # starting the thread for func2


# output:
# Function 1
# Function 2
# Function 1
# Function 2
# Function 1
# Function 2
# Function 1
# Function 2
# Function 1
# Function 2




print("Using class to create threads working with threading module in simultaneously")

from threading import *
from time import sleep

class A(Thread): # creating a class A that inherits from Thread class
    def run(self):
        for i in range(5):
            print("Function A", current_thread().name) # printing the name of the current thread
            sleep(1)

class B(Thread): # creating a class B that inherits from Thread class
    def run(self):
        for i in range(5):
            print("Function B", current_thread().name) # printing the name of the current thread
            sleep(1)



obj1 = A() # creating an object of class A
obj2 = B() # creating an object of class B

# obj1.start() this call run method so we need to override the run method in class A and class B to call the func method in both classes
obj1.start()
sleep(0.1) # adding a small delay to ensure that func1 starts before func2
obj2.start()
print("bye",current_thread().name) 
# this will print before the threads finish executing because the main thread is not waiting for the child threads to finish.

# output:
# Function A Thread-1
# Function B Thread-2
# bye MainThread
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2

# obj1.start() this call run method so we need to override the run method in class A and class B to call the func method in both classes
obj1.start()
sleep(0.1) # adding a small delay to ensure that func1 starts before func2
obj2.start()

obj1.join() # this will make the main thread wait for obj1 to finish before moving on to the next line of code
obj2.join() # this will make the main thread wait for obj2 to finish before moving on to the next line of code


print("bye",current_thread().name) 
# this will print before the threads finish executing because the main thread is not waiting for the child threads to finish.



# output:
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# Function A Thread-1
# Function B Thread-2
# bye MainThread



# when we call join() method on a thread,
# it will block the main thread until the thread on which join() is called finishes its execution.







############# Synchronization in Python ##############


print("Synchronization in Python")







from threading import *
from time import sleep




def display():
    for i in range(5):
        print(current_thread().name, "is displaying", i)
        sleep(1)


display() # this will execute the display function in the main thread and it will block the main thread until the display function finishes executing

t1 = Thread(target=display) # creating a thread for display function
t2 = Thread(target=display) # creating another thread for display function
t1.start() # starting the thread for display function
t2.start() # starting the thread for display function
t1.join() # this will make the main thread wait for the display thread to finish before moving on to the next line of code
t2.join() # this will make the main thread wait for the display thread to finish before moving on to the next line of code
print("Display function has finished executing") # this will print after the display thread has finished executing

# when run same method in multiple threads, 
# it will execute the method in both threads simultaneously and 
# the output will be interleaved because both threads are running at the same time.

'''
output:
MainThread is displaying 0
MainThread is displaying 1
MainThread is displaying 2
MainThread is displaying 3
MainThread is displaying 4
Thread-1 (display) Thread-2 (display)is displaying is displaying  00

Thread-2 (display)Thread-1 (display)  is displaying 1is displaying
 1
Thread-2 (display) is displaying 2
Thread-1 (display) is displaying 2
Thread-2 (display) is displaying 3
Thread-1 (display) is displaying 3
Thread-2 (display) is displaying 4
Thread-1 (display) is displaying 4
Display function has finished executing

'''


# to prevent this 
print("Using Lock to prevent interleaving of output when using one resource in multiple threads")


from threading import *
from time import sleep


lock = Lock() # creating a lock object so we get primary method aquire and release method to acquire and release the lock

# when calling aquire() method, the thread will wait until the lock is available and then it will acquire the lock and execute the code inside the with block.
# when calling release() method, the thread will release the lock and other threads can acquire the lock and execute the code inside the with block.

def display():
    lock.acquire() # acquiring the thread before executing the code inside the with block
    for i in range(5):
        print(current_thread().name, "is displaying", i)
        sleep(1)
    lock.release() # releasing the thread after executing the code inside the with block



t1 = Thread(target=display) # creating a thread for display function
t2 = Thread(target=display) # creating another thread for display function
t1.start() # starting the thread for display function
t2.start() # starting the thread for display function

'''
output:
Thread-1 (display) is displaying 0
Thread-1 (display) is displaying 1
Thread-1 (display) is displaying 2
Thread-1 (display) is displaying 3
Thread-1 (display) is displaying 4
Thread-2 (display) is displaying 0
Thread-2 (display) is displaying 1
Thread-2 (display) is displaying 2
Thread-2 (display) is displaying 3
Thread-2 (display) is displaying 4
'''