"""
Practice Python - Exercise 07: List Comprehensions

This script takes a predefined list of numbers and filters out all the odd
numbers, creating a new list containing only the even numbers. It accomplishes
this using a single-line Python list comprehension.

Exercise URL: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
"""

# Initial list of mixed even and odd integers (squares from 1 to 10)
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension: iterates through 'a', filters using the modulo operator
# (num % 2 == 0), and extracts only the even elements into a new list.
even = [num for num in a if num % 2 == 0]

# Output the resulting filtered list
print(even)
