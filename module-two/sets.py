# Sets are special collection data type in Python
# Useful for storing unique items. 
# Unordered: You wont know the order of elements.
# Mutable: You can change the set's contents by addidg or removing items.
# No indexing: Unlike lists or tuples, sets don't have a defined order.
# So you can't access items using an index.

# Creating an Empty Set.
# Example:

empty_set = set() 
print(type(empty_set)) # Output: <class 'set>

# Creating a set with values.
# We can create a set by listing its values inside curly braces.
# Sets automatically remove any duplicate values:

new_set = {'one', 'two', 'three'}
print(new_set) # Output: {'one', 'two', 'three'}

# Working with Lists, Tuples and Dictionaries:
# Sets are also great for removing duplicates from other data structures. 
# For example, you can convert a list into a a set to eliminate duplicate values:

alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist) # Converting list to a set
print(set_list) # Output: {'stuff', 'item', 'thing', 'oddity'}

#  Engage & Apply: Creating Sets: 
# Exercise 1: Practice Creating Sets
# Create a list of your favorite hobbies, making sure to repeat a few of them.
# Convert the list into a set to automatically remove the duplicates.
# Print both the original list and the set to compare.

list_hobbies = ['soccer', 'basketball', 'coding', 'coding', 'working out', 'reading']
set_hobbies = set(list_hobbies)
print(list_hobbies)
print(set_hobbies)

# Exercise 2: Loop Through a Set
# Create a set of your top 5 favorite books or movies.
# Write a for loop to print each item in the set.

favorite_movies = {'The Dictator', 'Anaconda', 'Sky High', 'Scary Movie Series', 'Rush Hour Series'}
for i, movie in enumerate(favorite_movies, 1):
    print(f"{i}. {movie}")
    
# Set Methods: 
# Membership checks: You can quickly check if an item exists in a set using the in keyword. 
# This is one of the most useful features of sets, as it is extremly effiecient. 

#Example: checking membership

my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
print('superman in' in my_set) # Output: True
print('Spiderman' in my_set) # Output: False 
# Membership checks happen alomost instantaneously, making sets ideal when you need to check
# Whether a value exists in a collection. 

# Adding items to a set:
# Sets are mutable, so we can add new elements using the .add() method. If you try to add
# an element that already exists in the set, it will simply be ignored.

# Example: Adding an item

my_set.add('green lantern')
print(my_set) # Output: {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

# Exercise 3: Set Modification Practice
# Create a set of at least 4 of your favorite foods.
# Add one more food item to the set.
# Write code to check if a specific food item is in the set, then print the result.

favorite_foods = {'tuna sandwich', 'rice & goat meat', 'outmeal', 'cheesy bean and rice burrito'}
favorite_foods.add('triple cheese burger')
print('hamburger' in favorite_foods)
print(favorite_foods)