# in Python you don't need to define the data type.

# Variables can be reassigned

# Strings:
name = "Samir"

# integers 
age = 9

# floats
temp = 87.98

# Boolean
is_logged_in = True
is_admin = False
age = 25
print(age)

# print to the terminal
print(name, age, temp, is_logged_in, is_admin) 

# Arithmetic Operations 
print( 5 + 10)
print(5 - 10)
print(5 * 10)
print( 5 / 10 )

# Modulus: The remainder of the division 
print(519 % 2)

# Comparison Operators
# Compare values, they return true or false

# Equal
print( 5 == 5)
print(4 == 5)

# Not Equal

print(4 != 5)

# Greater than 
print(8 > 10)

print(age > 19)

# Greater than or equal

print(age >= 18)

# Less than 

print(9 < 6)

# Less than or equal

print(8 <= 10 )

# User Input
# Programs often need input from users
# Allows the program to be interactive

name = input("Enter your name: ")
age = input("Enter your age: ")

# String Concatenation 
print("Hello,", name, "You're", age, "years old.")
print(f"Hello, {name}. You're {age} years old")

# Conditional Statements
# Programs often need to make decisions

age = 20 

# Python uses indentation instead of braces

if age >= 18:
    print("You're an adult")
    
else:
    print("You cannot vote yet")


# Multiple Conditions
# Python Checks conditions top to bottom

score = 3

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >=70:
    print("Grade C")
else:
    print("You need improvement")
    
# Logical Operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")
    
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
    
# Calculator App
# To check type: print(type(num1))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2 

print(f"The result: {total}")

# Grade calculator App

score = int(input("Enter your exam score: "))
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Great job")
elif score >= 70:
    print("Good effort")
else:
    print("Keep practicing")

