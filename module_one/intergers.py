# Calculate the total cost of the following items. 
# Then, apply a 10% discount and display the final amount

milk = 5
eggs = 3
coffee = 10

total = milk + eggs + coffee
discount = total * 0.10
discounted = total - discount

print(f"Total cost of all items is: {total}")
print(f"Final amount after 10% discount: {discounted}")

#Design a simple calculator that performs operations on two integers provided by the user.

number_one = int(input("Please enter a number: "))
number_two = int(input("Please enter another number: "))

add = number_one + number_two
subtract = number_one - number_two
multiply = number_one * number_two
divide = number_one / number_two
divide_floor = number_one // number_two

print(f" {number_one} + {number_two} = {add}")
print(f" {number_one} - {number_two} = {subtract}")
print(f" {number_one} * {number_two} = {multiply}")
print(f" {number_one} / {number_two} = {divide}")
print(f" {number_one} // {number_two} = {divide_floor}")
