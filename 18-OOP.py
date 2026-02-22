# obejecty oriented programming

# basic unit of oop is class
# class is a blueprint for creating objects
# when creating function inside the class its called method
# object has attributes (data) and methods (functions)


# object (class) - mobile phone
# attribute - color, brand, model, price
# method - make_call(), send_message(), take_photo()






class MobilePhone:
    def send_message(self):
        print(f"Hello, this is a message from your mobile phone.")


phone1 = MobilePhone() # phone1 is an object of MobilePhone class to access attributes and methods and constructors method is MobilePhone()
phone1.send_message() # calling the method using the object





class MobilePhone:
    def send_message(self, name):
        print(f"Hello, this is a message from your mobile phone {name}.")


phone1 = MobilePhone()
phone1.send_message("Apple") 
# output: Hello, this is a message from your mobile phone Apple.

phone2 = MobilePhone()
phone2.send_message("Samsung")
# output: Hello, this is a message from your mobile phone Samsung.




# self parameter is a reference to the current instance of the class
class MobilePhone:
    def send_message(self, name):
        self.x = name
        print(f"Hello, this is a message from your mobile phone {name}.")


phone1 = MobilePhone()
phone1.send_message("Apple") 
phone1.x # when we assign a value to self.x, it becomes an attribute of the object phone1
# we can use self keyword to inside class attributes to connect with the object itself
# output: Hello, this is a message from your mobile phone Apple.
print(phone1.x)  # output: Apple


phone1.x = "New Apple"
print(phone1.x)  # output: New Apple
# we can also modify the attribute value outside the class using the object









############### __init__()  ###############

class MobilePhone:
    # constructor method to initialize attributes
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    # method to make a call
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    # method to send a message
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    # method to take a photo
    def take_photo(self):
        print(f"Taking photo with {self.brand} {self.model} camera.")


ApplePhone = MobilePhone("Apple", "iPhone 13", "Black", 999)
SamsungPhone = MobilePhone("Samsung", "Galaxy S21", "White", 799)

ApplePhone.make_call("+1234567890")
SamsungPhone.send_message("+0987654321", "Hello from my Samsung phone!")
ApplePhone.take_photo()

# output:
# Calling +1234567890 from Apple iPhone 13...
# Sending message to +0987654321: Hello from my Samsung phone!
# Taking photo with Apple iPhone 13 camera.

print(ApplePhone.color)  # output: Black
print(SamsungPhone.price)  # output: 799
print(ApplePhone.brand)  # output: Apple
print(SamsungPhone.model)  # output: Galaxy S21


# we can access the attributes using the object and dot notation
ApplePhone.price = 899  # modifying the attribute value
print(ApplePhone.price)  # output: 899
SamsungPhone.color = "Blue"  # modifying the attribute value
print(SamsungPhone.color)  # output: Blue

# why using self keyword in the __init__() method?
# self keyword is used to refer to the current instance of the class, it is used to access the attributes and methods of the class, it is also used to initialize the attributes of the class, 
# it is a convention to use self as the first parameter of the __init__() method, 
# but we can use any name instead of self, 
# but it is not recommended to use any other name than self 
# because it is a convention and it makes the code more readable and understandable.
