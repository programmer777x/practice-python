"""
Practice Python - Exercise 10: List Overlap Comprehensions

This script finds the common elements between two lists and returns a new
list containing only the unique overlapping items, avoiding duplicates.

Exercise URL: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
"""


def main():
    """
    Executes the list overlap comparison using nested loops and prints
    the resulting list of unique common elements.
    """

    # Clear a line to separate the game from the terminal execution path
    print()

    # Predefined test data provided by the exercise
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = []

    # Iterate through both lists to find overlapping elements without duplicates
    for i in a:
        for j in b:
            if j == i:
                if j not in c:
                    c.append(j)

    print(c)


# Ensures the game only runs when this script is executed directly (not imported)
if __name__ == "__main__":
    main()
