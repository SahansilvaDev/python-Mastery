import pickle

data = {'name': 'kamal', 'age': 20, 'weight': 56.2}

# wb - write binary mode
with open('44-PickleModule/data.pkl', 'wb') as f:
    pickle.dump(data, f)


# rb - read binary mode - loading the data back
# import os
# print(os.getcwd())

# os.chdir('44-PickleModule') # changing the current working directory to 44-PickleModule

with open('44-PickleModule/data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)  # output: {'name': 'kamal', 'age': 20, 'weight': 56.2}

    print(loaded_data['name'])  # output: kamal


