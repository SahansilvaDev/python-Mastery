
####################### PRIVATE Variables ######################

class myClass:
    x=10
    __y = 20  # private variable


myObj = myClass()
print(myObj.x)  # output: 10
# print(myObj.__y)  # AttributeError: 'myClass' object has no attribute '__y'
#because __y is private variable and cannot be accessed outside the class




class myClass:
    x=10
    __y = 20  # private variable

    def get_y(self):
        return self.__y  # accessing private variable inside the class

myObj = myClass()
print(myObj.x)  # output: 10

print(myObj.get_y())  # output: 20
# accessing private variable using a public method inside the class





####################### PRIVATE Methods ######################


class myClass:
    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        self.__private_method()  # accessing private method inside the class

myObj = myClass()
myObj.public_method()
# output:
# This is a public method
# This is a private method





