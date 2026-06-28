"""
Practice Python - Exercise 09: Guessing Game One

A command-line number guessing game where the player attempts to guess
a randomly generated number between 1 and 9, tracking total attempts.

Exercise URL: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""

import random

# Generate the target number and initialize the guess counter
random_number = random.randint(1, 9)
guesses = 0

# Take the initial guess from the user
user_guess = int(input("Guess a number between 1 and 9: "))
guesses += 1

# Game loop to provide feedback and accept new guesses until correct
while True:
    if random_number == user_guess:
        print("You guessed the number!")
        break
    elif random_number > user_guess:
        user_guess = int(input("Your guess is too low, try again: "))
    else:
        user_guess = int(input("Your guess is too high, try again: "))

    guesses += 1

# Display final stats
print(f"\nGuesses: {guesses}\nThanks for playing.")
