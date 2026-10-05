import random 

#Create a string with a sentence of your choice

sentence = "  Samir is a Software Developer.  "

print(sentence.upper())
print(sentence.strip())
print(sentence.replace("Developer", "Engineer"))
print(sentence.split())

#Build a text-based name generator that combines random first and last names using string manipulation.

first_names = ["Samir", "Sam", "Sammy"]
last_names = ["Lander", "World", "Supremacy"]

import random

f_name = random.choice(first_names)
l_name = random.choice(last_names)
print(f"{f_name} {l_name}")