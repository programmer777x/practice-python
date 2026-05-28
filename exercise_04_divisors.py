"""
Practice Python - Exercise 04: Divisors

This script prompts the user for an integer, generates a range of
possible numbers from 1 up to the chosen number, and uses a list
comprehension with the modulo (%) operator to filter out all exact divisors.

Exercise URL: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""


print()


# Prompt the user for an integer to analyze
num = int(input('Please choose a number to divide: '))

# Generate a list of numbers from 1 to num (inclusive) to test as potential divisors
test_list = list(range(1, num + 1))
divisor_list = []

# Method 1
# Loop through the test list to identify exact divisors
# for divisor in test_list:
#     if num % divisor == 0:
#         divisor_list.append(divisor)

# Method 2
# Use a list comprehension to filter the test list in a single line.
# It only keeps the 'divisor' if 'num % divisor == 0' evaluates to True.
divisor_list = [divisor for divisor in test_list if num % divisor == 0]

print()
# Note: Keeping the original test list print statement commented out for debugging reference
# print(test_list)

# Output the final list of verified divisors
print(f"Divisors of {num}: {divisor_list}")
