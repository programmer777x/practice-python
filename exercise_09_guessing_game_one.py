"""
Practice Python - Exercise 09: Guessing Game One

A command-line number guessing game where the player attempts to guess
a randomly generated number between 1 and 9, tracking the number of guesses.

Exercise URL: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""

import random

# Clear a line to separate the game from the terminal execution path
print()

def input_validator(current_guess, valid_list):
    """Repeatedly prompts the user until a valid guess or exit command is provided."""
    while current_guess not in valid_list:
        print("\nInvalid input, please try again.")
        current_guess = input("Guess a number between 1 and 9 (exit to quit): ")

    return current_guess

# Generate the target number and initialize the guess counter
random_number = random.randint(1, 9)
guesses = 0

# Create validation list: ['1', '2', ..., '9', 'exit']
guess_validator = [str(i) for i in range(1, 10)]
guess_validator.append("exit")

# Take the initial guess from the user
user_guess = input("Guess a number between 1 and 9 (exit to quit): ")
user_guess = input_validator(user_guess, guess_validator)

# Game loop: provide high/low feedback and accept new guesses until correct or exit
while user_guess != "exit":
    print()
    guesses += 1
    user_guess_int = int(user_guess)

    if random_number == user_guess_int:
        print("You guessed the number! 🎉")
        break
    elif random_number > user_guess_int:
        user_guess = input("Your guess is too low, try again: ")
    else:
        user_guess = input("Your guess is too high, try again: ")

    user_guess = input_validator(user_guess, guess_validator)

# Display final game statistics
print(f"\nGuesses: {guesses}\nThanks for playing.")
