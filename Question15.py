# Initializing dictionary
test_dict = {"Prteek": 22, "Ankur": 21, "Ashish": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Ankur
del test_dict["Ankur"]

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)

# Using del to remove a dict
# raises exception
#del test_dict["Ankur"]
