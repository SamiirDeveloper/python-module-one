#Manipulate Python lists, their characteristics and operations.

fruit = ["apple", "banana", "cherry", "date"] # Creating a list

fruit.append("elderberry") #Items items to the end of the list
fruit.insert(1, "blueberry") #Inserting items at an specific index
fruit.remove("banana") #Removing items
del fruit[0] # Deleting items

citrus_fruits = fruit[1:3] #Slicing a list
print(citrus_fruits)

print(fruit)
print(fruit[0])
print(fruit[-1])

# Create a program that asks the user for their top 3 favorite books, 
# stores them in a list prints the list in a sorted list.

favorite_books = [] #initialize an empty list

first_book = input("What is the first book you would like to add?: ") #Prompt user for an input
second_book = input("What is the second book you would like to add?: ")
third_book = input("What is the third book you would like to add?: ")

favorite_books.append(first_book) #Add books to list
favorite_books.append(second_book)
favorite_books.append(third_book)

favorite_books.sort() # Sort books in alphabetical order
print(favorite_books) #Print Books 
