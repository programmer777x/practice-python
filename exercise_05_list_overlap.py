"""
Practice Python - Exercise 05: List Overlap

This script finds common elements between two lists without duplicates.
It covers three approaches:
1. Main Goal: A custom function using nested loops and membership checks.
2. Extra 1: Generating and comparing two randomly sized and populated lists.
3. Extra 2: Utilizing Python sets and the .intersection() method for a one-liner solution.

Exercise URL: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
"""


print()


import random


# Initial static data for the Main Goal
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []


def compare(a, b, c):
    """Loops through list 'a' and adds elements to 'c' if they exist in 'b' and aren't duplicates."""
    for element in a:
        if element in b:
            if element not in c:
                c.append(element)

def output(c):
    """Helper function to cleanly print the result list or a fallback message if empty."""
    if len(c) > 0:
        print(f"Common elements: {c}")
    else:
        print('No common elements')


# ==========================================
# --- Main Goal ---
# ==========================================

compare(a, b, c)

# Note: Retaining manual verification tests for debugging history
# print(3 in a)
# print(4 in a)

print('--- Main Goal ---\n')
print(f"Common elements: {c}")


# ==========================================
# --- Extra 1 (Randomly Generated Lists) ---
# ==========================================

# Determine random list sizes between 15 and 20 elements
a_size = random.randint(15, 20)
a = []
b_size = random.randint(15, 20)
b = []

# Define standard range bounds for the random numbers
RANGE_MIN = 1
RANGE_MAX = 100

# Populate and sort list 'a'
for i in range(a_size):
    a.append(random.randint(RANGE_MIN, RANGE_MAX))
a.sort()

# Populate and sort list 'b'
for i in range(b_size):
    b.append(random.randint(RANGE_MIN, RANGE_MAX))
b.sort()

print('\n--- Extra 1 ---\n')
print(f"List a: {a}")
print(f"List b: {b}")

# Reset results list and perform the comparison using the custom function
c = []
compare(a, b, c)

print()
output(c)


# ==========================================
# --- Extra 2 (Set Intersection Optimization) ---
# ==========================================

print('\n--- Extra 2 ---\n')
print(f"List a: {a}")
print(f"List b: {b}")

# Convert lists to sets to utilize built-in, highly optimized intersection logic
set_a = set(a)
set_b = set(b)
c = list(set_a.intersection(set_b))
c.sort()  # Sort the results since sets do not preserve sequence order

print()
output(c)
