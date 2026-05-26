"""
Practice Python - Exercise 01: Character Input

This script asks the user for their name, age, and a number of copies. 
It dynamically calculates the exact calendar year they will turn 100 
years old using the current year from the datetime module, then prints 
out the message the specified number of times.

Exercise URL: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""


# Import datetime to automatically fetch the current year (prevents hardcoding dates)
from datetime import datetime


print()

# --- User Input ---
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
amount_to_print = int(input("Enter how many times to print the results: "))

# Get the current 4-digit calendar year dynamically
current_year = datetime.now().year

# --- Logic & Formatting ---
# Calculate the target year: (100 - age) gives years remaining, then add to current year
results = f"{name}, you will turn 100 years old in the year {100 - age + current_year}"

# --- Archived / Previous Test Lines ---
# The following lines were used during initial testing to verify inputs and logic:
# print("\nYour name is " + name)
# print("You are " + age + " year(s) old")
# print(f"{name}, you will turn 100 years old in the year {100 - age + 2026}")

# Use string multiplication to repeat the message, adding a newline (\n) so each prints on its own line
print()
print(amount_to_print * f"{results}\n")
