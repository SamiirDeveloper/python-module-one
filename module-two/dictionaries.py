# Python dictionaries are a versatile data structure used to store data in key-value pairs.
# They allow you to organize and access data efficiently, much like a real-world dicionaries.
# Where you can quickly look up information using a key (Which can be various data types, such as strings, numbers or tuples).
# In Python, dictionaries are especially useful for associating data with unique identifiers, making them great for scenarios like 
# looking up user profiles by username, storing configuraton settings, or managing inventory by product ID.

# Dictionaries in Python are defined using curly braces {} and consist of key-value pairs.
# Each key in a dictionary must be unique and immutable (e.g., strings, numbers, or tuples)
# While the values can be of any data type and can be duplicated. Starting from Python 3.7,
# Dictionaries maintain insertion order, which became a part of the language specification in Python 3.8
# They are also mutable, meaning you can modify them after they are created.

# Example of Python dictionary

my_dict = {
    'name': 'Samir',
    'age': 99,
    'city': 'Seattle'
    
}

# In this example, the dictionary my_dict contains three key-value pairs.
# The keys are 'name', 'age', and 'city', and their respective values are 'Samir', 99, and 'Seattle'.

# Accessing Values in a dictionary
# You can access the values stored in a dictionary by using the keys.

# Example:

my_dict = {
    'name': 'samir',
    'age': 99,
    'city': 'Seattle'
}

print(my_dict['name']) # Output: 'Samir'

# The .get() method & avoiding missing keys.
# If you try to access a key that does not exist, Python will raise a KeryError. To avoid this,
# You can use the .get() method, which will return None (or a default value you specify)if the key doesn't exist.

# The .get() method is particularly useful for preventing errors when acessing keys that may or may not be in the dictionary.

my_dict = {
    'name': 'Samir',
    'age': 99,
    'city': 'Seattle'
}

print(my_dict.get('age')) # Output: 99
print(my_dict.get('address', 'Not Available')) # Output: Not available

# Adding, Modifyingm and Removing Elements.
# Dictionaries are dynamic, meaning you can add, modify or remove elements at anytime.

# Adding elements: To add a new key-value pair, simply assign a value to anew key.
# Lets add a new key to the my_dict dictionary from our previous example:

my_dict['profession'] = 'Engineer'
print(my_dict)
# In this example, the key 'profession with the value 'Engineer' is added to the dictionary. 

# Modifying Elements: To modify an existing value, assign a new value to an existing key.
# Continuing with our previous example:

my_dict['age'] = 98
print(my_dict)

# Removing Elements: You can use the del statement or the .pop() method to remove elements from a dictionary.

del my_dict['city']
print(my_dict)

# Alternatively, .pop() allows you to remove an item and also return its value, which can be useful 
# if you need to use it elsewhere in your code.

removed_value = my_dict.pop('profession')
print(removed_value) # Output: Engineer 

# Dictionary Methods: Dictionaries come with many useful methods that help you interact with their data.
# .keys(): returns a view object that displays a list of all the keys in the dictionary.
# It can be converted to a list if needed. 

for key in my_dict.keys():
    print(key)

print(list(my_dict.keys())) # Output: ['name', 'age']

# .values(): Returns a view object of all the values in the dictionary.

print(list(my_dict.values())) # Output: [('name', 'Samir'), ('age', 26)]

# .items(): Returns a view object that displays a list of key-value tuple pairs.

print(list(my_dict.items())) # Output: [('name', 'Alice'), ('age', 26)]

