# # Common exception types:
# # 1. ZeroDivisonError: Trying to divide by zero.
# # 2. TypeError: An Operation or function is applied to an object of inappropriate type.
# # 3. ValueError: A function recieves an argument of the right type but inappropriate type

# # Syntax Error

if True:
    print("Hello") #missing colon at the end of if statement
    
# # Runtime exception 
x = 1 / 0 # This will raise ZeroDivisionError

# # Basic Exception Handling with try and except
# # The try blocks lets you test a block of code for errors,
# # While the except block lets you handle the error

# # Example:

try:
    x = 10 /0
except ZeroDivisionError:
    print("You can't divide by zero!")
    
    
# # Write a program that prompts the user for two numbers,
# # then divides the first by the second. Handle the exceptions
# # Where the user enters invalid data (non-numeric) or tries to divide by zero.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    
except ValueError:
    print("Please enter numbers only!")
    
except ZeroDivisionError:
    print("You can't divide by zero.")
    
print(f"{num1} Divide by {num2} = {result}")

# # Catching multiple exceptions 
# # You can handle multiple exceptions by specifying multiple except blocks
# # Or catching multiple exceptions in a single block

# # Example: 

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    
except ValueError:
    print("That's not a valid number!")
    
# except ZeroDivisionError:
#     print("You cant divide by zero!")
    
# # Catching multiple exceptions in one block

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occured: {e}")
    
print(f"{result}")

# # else and finally clauses
# # The else block is executed if no exception occur in the try block.
# # The Finally block is executed no matter what, regardless of whether an exception occured. 

# # Example with else and finally:

try:
    x = int(input("Enter a number: " ))
    result = 10 / x
    
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occured: {e}")

else:
    print(f"The result is {result}")

finally: 
    print("Execution complete!")
    
    
# Create a program that simulates an ATM withdrawal process. 

account_balance = 1500



try:
    amount_withdrawn = int(input("Enter withdrawal amount: "))
    result = account_balance - amount_withdrawn
    if amount_withdrawn > account_balance:
        print("Insufficient balance!")
    else:
        print(f"Your balance is: {result}")
    
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occured: {e}")
    
finally:
    print("Thank you for your business!")     