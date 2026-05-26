"""
Practice Python - Exercise 02: Odd Or Even

This script takes two integer inputs from the user and performs
the following conditional checks using the modulo (%) operator:
1. Verifies if the first number is evenly divisible by the second number.
2. Checks if the first number is a multiple of 4.
3. Determines if the first number is otherwise odd or even.

Exercise URL: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
"""


print()

# --- Setup and User Input ---

# Prompt the user for two numbers to analyze and convert inputs to integers
num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

print()

# --- Conditional Logic / Checks ---

# Priority 1: Check if the custom 'check' number divides into 'num' perfectly
if num % check == 0:
    print(f"The number {num} is divisible by {check}.")

# Priority 2: Check if 'num' is a specific multiple of 4
elif num % 4 == 0:
    print(f"{num} is a multiple of 4.")

# Priority 3: Fallback to basic parity (odd vs even) if previous checks fail
else:
    # A remainder greater than 0 means the number is odd
    if num % 2 > 0:
        print(num, "is odd.")
    else:
        print(num, "is even.")
