"""
Practice Python - Exercise 10: List Overlap Comprehensions

This script finds common elements between two predefined lists using a nested
list comprehension and ensures the final output contains unique values.

Exercise URL: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
"""


def main():
    """
    Execute the list overlap comprehension and print unique common elements.
    """

    # Clear a line to separate the game from the terminal execution path
    print()

    # Predefined test data provided by the exercise
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Nested loop checks for matches; set() removes duplicates from the result
    print(list(set([j for i in a for j in b if j == i])))


# Ensures the script only runs when executed directly (not imported as a module)
if __name__ == "__main__":
    main()
