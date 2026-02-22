from logger import logging


def add(x,y):
    result = x + y
    logging.info(f"Adding {x} and {y} to get {result}")
    return result

def subtract(x,y):
    result = x - y
    logging.info(f"Subtracting {y} from {x} to get {result}")
    return result

def multiply(x,y):
    result = x * y
    logging.info(f"Multiplying {x} and {y} to get {result}")
    return result
    
def divide(x,y):
    try:
        result = x / y
        logging.info(f"Dividing {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero is not allowed.")    
        return "Division by zero is not allowed."
