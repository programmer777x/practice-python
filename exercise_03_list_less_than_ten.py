"""
Practice Python - Exercise 03: List Less Than Ten

This script manipulates a list of numbers to filter out elements
based on specific numerical conditions (less than 5, and less than
a user-defined threshold) using both standard loops and list comprehensions.

Exercise URL: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""


print()


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


# --- Main Goal ---
# Loop through the list and print out all elements less than 5 individually

for element in a:
    if element < 5:
        print(element)

print()


# --- Extra 1 ---
# Instead of printing one by one, append the elements to a new list and print the list

for element in a:
    if element < 5:
        b.append(element)

print(b)
print()


# --- Extra 2 ---
# Write the filtering logic in one line of Python using a list comprehension

print([x for x in a if x < 5])
print()


# --- Extra 3 ---
# Ask the user for a number, then print a list of all elements smaller than that number

b = []  # Reset the list to clear out the previous exercise data

num = int(input("Enter a number: "))
print()

for element in a:
    if element < num:
        b.append(element)

print(b)
