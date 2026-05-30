"""
Practice Python - Exercise 06: String Lists

This script prompts the user for a string and determines whether it reads
the same forward and backward. It showcases two distinct approaches:
1. Method 1: The native Pythonic way using string slicing (`[::-1]`).
2. Method 2: A manual, iterative approach building a new string from the back.

Exercise URL: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""


print()


def palindrome_check(string, string_reversed):
    """Compares the original and reversed strings to print a formatted result."""
    output = f"'{string}' is"

    if string != string_reversed:
        output += ' not'

    output += ' a palindrome.'
    print(output)


# Get user input for evaluation
string = input("Enter a string: ")


# ==========================================
# --- METHOD 1: String Slicing ---
# ==========================================

# Uses Python's built-in step slicing `[start:stop:step]` with a step of -1
# to efficiently reverse the entire string.
string_reversed = string[::-1]

print(f"String reversed: {string_reversed}")
print('\n--- METHOD 1 ---')
palindrome_check(string, string_reversed)


# ==========================================
# --- METHOD 2: Manual Iteration ---
# ==========================================

def reverse(string):
    """Reverses a string manually by looping backwards through its indices."""
    string_reversed = ''

    # Loop through the length of the string and calculate the backward index
    for i in range(len(string)):
        string_reversed += string[len(string)-1-i]

    return string_reversed


string_reversed = reverse(string)
print('\n--- METHOD 2 ---')
palindrome_check(string, string_reversed)


# ==========================================
# --- UNIT TESTS (Historical Verification) ---
# ==========================================

# Retaining commented-out basic test cases used during development.
# test_string_one = "string"
# test_string_two = "abcba"
# test_string_three = "abccba"
#
# string_reversed = test_string_one[::-1]
# print(f"\n\nTest string one: {test_string_one}")
# print(f"Test string one reversed: {string_reversed}")
# print(f"Palindrome: {test_string_one == string_reversed}")
#
# string_reversed = test_string_two[::-1]
# print(f"\nTest string two: {test_string_two}")
# print(f"Test string two reversed: {string_reversed}")
# print(f"Palindrome: {test_string_two == string_reversed}")
#
# string_reversed = test_string_three[::-1]
# print(f"\nTest string three: {test_string_three}")
# print(f"Test string three reversed: {string_reversed}")
# print(f"Palindrome: {test_string_three == string_reversed}")
