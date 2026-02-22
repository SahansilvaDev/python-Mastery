# first install 
# pip install python-dotenv


import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the API key from environment variable
api_key = os.getenv("API-KEY")
print(f"API Key: {api_key}")


# https://pypi.org/project/python-dotenv/


# import os
# from dotenv import load_dotenv
# _ = load_dotenv()
'''

What it does:

Loads environment variables using load_dotenv().
Does not explicitly retrieve or use any environment variables in the code.
The _ is used as a throwaway variable to indicate that the return value of load_dotenv() is not being used.
Use case: This snippet is useful when you only need to load environment variables into the process's environment (e.g., for other parts of the code to use) but do not need to directly access them in this part of the code.


'''