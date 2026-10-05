# Design a program that will help someone decide between
#two activities based on the weather and mood.
import random

weather = input("Weather type: Sunny or Raining?: ")
mood = input("Enter your mood: Happy or Tired?: ")

if weather.lower() == "sunny" and mood.lower() == "happy": 
    print("Go for a hike!")
else:
    print("Relax indoors")
    
    
# Write a program where the user has to guess a secret
# number between 1 and 10. The program should 
# provide feedback if the guess is too high or too low and
# congratulate the user if the guess correctly.  

secret_number = random.randint(1,10)
guess = int(input("Please enter a number between 1 and 10: "))

if (secret_number == guess):
    print("Congratulations, You've guessed the correct number")
elif (guess < secret_number):
    print("Too Low")
else:
    print("Too high!")

