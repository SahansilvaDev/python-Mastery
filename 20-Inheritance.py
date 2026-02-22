###################### Inheritance ######################


class Animal: # parent class/super class
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):  # Dog class inherits from Animal class # child class/sub class
    def bark(self):
        return "Woof! Woof!"

dog1 = Dog()  # dog1 is an object of Dog class
print(dog1.speak())  # output: Animal speaks (inherited method)
print(dog1.bark())  # output: Woof! Woof!



class puppy(Animal,Dog):  # Cat class inherits from Animal class # multiple inheritance
    def barkS(self):
        return "MMMMM!"
puppy1 = puppy()  # cat1 is an object of Cat class
print(puppy1.speak())  # output: Animal speaks (inherited method)
print(puppy1.bark())  # output: Woof! Woof! (inherited method)
print(puppy1.barkS())  # output: MMMMM! (own method)

######Multilevel Inheritance#######

class Animal: # parent class/super class
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):  # Dog class inherits from Animal class # child class/sub class
    def bark(self):
        return "Woof! Woof!"


class puppy(Dog):  # Cat class inherits from Animal class # multiple inheritance
    def barkS(self):
        return "MMMMM!"
    

puppy1 = puppy()  # cat1 is an object of Cat class

print(puppy1.speak())  # output: Animal speaks (inherited method)
print(puppy1.bark())  # output: Woof! Woof! (inherited method)
print(puppy1.barkS())  # output: MMMMM! (own method)


###################### super() Function ######################


class A:
    def method_A(self):
        print("Method A from class A")

class B(A):
    def method_B(self):
        super().method_A()  # calling method_A from class A using super()
        print("Method B from class B")

obj1 = B()
obj1.method_B()  # output: Method B from class B
# output:
# Method A from class A
# Method B from class B


###################### Method Overriding ######################


class A:
    def method_A(self):
        print("Method A from class A")

class B(A):
    def method_B(self):
        print("Method B from class B")

    def method_A(self):  # overriding method_A from class A
        print("Overridden Method A from class B")

obj1 = B()
obj1.method_A()  # output: Overridden Method A from class B







class Fruit:
    item = None  # class variable to keep track of number of items
    price = None  # class variable to keep track of unit price

    def set_values(self, x, y):
        self.item = x  # instance variable
        self.price = y  # instance variable

class Apple(Fruit):
    def price(self):
        print('For apple',self.item, 'units total price is:', self.price * self.item)

class Orange(Fruit):
    def price(self):
        print('For orange',self.item, 'units total price is:', self.price * self.item)


class Mango(Fruit):
    def price(self):
        print('For mango',self.item, 'units total price is:', self.price * self.item)


obj1 = Apple()
obj2 = Orange()
obj3 = Mango()

obj1.set_values(10, 15)
obj2.set_values(5, 20)
obj3.set_values(8, 25)

obj1.price() # output: For apple 10 units total price is: 150
obj2.price() # output: For orange 5 units total price is: 100
obj3.price() # output: For mango 8 units total price is: 200

