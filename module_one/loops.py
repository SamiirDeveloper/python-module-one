# Write a Python program that prints all the even numbers between 1 and 20 using a while loop.

even_numbers = 1
while even_numbers <= 20:
    if even_numbers % 2 == 0:
        print(even_numbers)
        
    even_numbers +=1
        
# Write a Python program that processes a range of
# numbers from 1 to 30. The program should do the following. 
# 1. Print all numbers from 1 to 30
# 2. Skip the numbers that are divisible by 3 using the continue statement
# 3. Stop the loop if the number is greater than 25 using break

# Using for loop
    
# for num in range(31): #Skip numbers that divisble by 3
#     if (num % 3 == 0):
#         continue
#     if (num > 25):
#         break
#     else:
#         print(num)
    
# While loop

nums = 1
while nums <= 30:
    if nums > 25:
        break
    
    if nums % 3 == 0:
        nums +=1
        continue
     
    print(nums)
    nums += 1
