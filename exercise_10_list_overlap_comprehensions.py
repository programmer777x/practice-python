"""
Practice Python - Exercise 10: List Overlap Comprehensions

This script dynamically generates two random lists of differing sizes and finds
their common unique elements using a flat list comprehension.

Exercise URL: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
"""

import random


def main():
    """
    Generate two unique random lists of different lengths and find their overlap.
    """

    # Insert a blank line to separate the program output from the terminal prompt
    print()

    # Define constraints for random number generation and list sizes
    POPULATION_MIN = 1
    POPULATION_MAX = 100
    ELEMENT_MIN = 10
    ELEMENT_MAX = 15

    list_a_size = random.randint(ELEMENT_MIN, ELEMENT_MAX)

    # Ensure list_b_size is explicitly a different length than list_a_size
    while True:
        list_b_size = random.randint(ELEMENT_MIN, ELEMENT_MAX)

        if list_b_size != list_a_size:
            break

    # Generate sorted lists of unique random numbers using the generated sizes
    a = sorted(random.sample(range(POPULATION_MIN, POPULATION_MAX),list_a_size))
    b = sorted(random.sample(range(POPULATION_MIN, POPULATION_MAX),list_b_size))

    # Debug print: Verify the generated lists and their respective lengths
    # print(f"{a}\n{len(a)}\n{b}\n{len(b)}\n")

    # Comprehension checks for matches; set() removes any potential duplicates
    c = list(set(item for item in a if item in b))

    # Display the result or a fallback message if no overlap exists
    if len(c) > 0:
        print(c)
    else:
        print("No matching elements.")


# Ensures the script only runs when executed directly (not imported as a module)
if __name__ == "__main__":
    main()
