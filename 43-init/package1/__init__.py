print("init file in package1")

from .module1 import fun1
from .module2 import fun2

def package_fun():
    print("Function in package1 from init file")