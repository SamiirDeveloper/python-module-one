# Functions are reusable blocks of code that perform a specific task
# We use functions to avoid duplication, improve readability and make debugging easier.

# Example:

def greet():
    print("Hello, Welcome to Coding Temple!")
    
# Defining a Function: Use the def keyword, followed by the function name and parenthesis ().
# Calling a function: To utilize/run the function, use its name followed by parentheses.

# Example: 

def greet():
    print("Hello, Welcome!")
    
greet() # -- > Hello, Welcome!
    
# Parameters and Arguments
#Parameters: Variables defined in the function declaration
#Arguments: Values passed into the function when its called

# Example:

def greet(name): # 'name' is a parameter
    print(f"Hello, {name}!")
    
greet("Alice") # 'Alice is an argument, output: Hello, Alice!



# Create a function introduce_yourself that takes a name and favorite hobby.
#The function should print a greeting and mention the persons hobby.

def introduce_yourself(name, hobby):
    print(f"Hello {name}, your hobby is {hobby}")

introduce_yourself("Samir", "Coding")
introduce_yourself("Sammy", "Sports")


# Return statements: Functions can return values using return keywords
#This is useful when you want to get an output from a function and use it later

# Example:

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result) # Output: 8



# Function Scope (Local vs Global Variables)
# Local Variables: Variables defined inside a function, only accessible within that function
# Global Variables: Variables defined outside any function and accessible throughout the code.

x = 10 # global variable

def print_number():
    x = 5 # local variable
    print(x) # Output: 5
    
print_number()
print(x) # Output: 10

# Default Parameters & Variable-Length Arguments
# Default parameters: Functions can have default values for paramters,
# Which are used if no argument is provided

def greet(name="Student"):
    print(f"Hello, {name}!")
    
greet() # Output: Hello, Student!
greet("Alice") # Output: Hello, Alice!


# Variable-Length Arguments: Use *args and **kwargs 
# to pass a variable number of arguments to function

def add_numbers(*args):
    return sum(args)

print (add_numbers(1, 2, 3)) # Output: 6
print(add_numbers(5, 10)) # Output: 15

# Create a function that takes a list of numbers as an argument,
# Squeres each number, and returns a new list with the squared values.

list_of_numbers = [3, 99, 12, 1, 7]

def squared_nums(nums_list):
    results_list = []
    
    for num in nums_list:
        squared_nums = num ** 2
        results_list.append(squared_nums)
    return results_list
        
print(squared_nums(list_of_numbers))

