
def add(a,b):
    return a + b


# print(add(15, 3))  # output: 18

# print(__name__)  # output: Mod2, 
# # because when a Python file is imported as a module,
# # the __name__ variable is set to the name of the module.

if __name__ == "__main__":
    print(add(15, 3))  # output: 18
    print(__name__)  # output: __main__, because when a Python file is run directly,
    # the __name__ variable is set to "__main__".