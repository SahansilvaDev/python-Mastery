######################### Virtual Environments in Python #########################
'''

To create and activate a virtual environment in Python on Windows:

1. Create a virtual environment:
Open your terminal and run:
python -m venv venv


This creates a folder named venv with the virtual environment.

2. Activate the virtual environment:
In the terminal, run:
venv\Scripts\activate


You should see (venv) at the start of your prompt, indicating the environment is active.

To deactivate:
Just run:
deactivate


'''
# pip list - to list all installed packages in the virtual environment

# pip freeze - to list all installed packages with their versions in the virtual environment

# pip freeze > requirements.txt 
# to save the list of installed packages with their versions to a file named requirements.txt

# pip install -r requirements.txt
# to install all the packages listed in the requirements.txt file with their specified versions in the virtual environment
