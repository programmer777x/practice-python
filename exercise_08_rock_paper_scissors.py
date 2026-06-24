"""
Practice Python - Exercise 08: Rock Paper Scissors

A command-line Rock, Paper, Scissors game played against the computer.
Includes input validation for user choices and an option to replay.

Exercise URL: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
"""


# print()


import random


# Valid options for the game and replay prompts
choices = ["rock", "paper", "scissor"]

while True:
    print()
    user_choice = input("Enter your choice (rock, paper, scissor): ")

    # Validate user input to ensure it matches game options
    while not user_choice in choices:
        print("\nInvalid choice!")
        user_choice = input("Enter your choice (rock, paper, scissor): ")
    print()

    # Generate random choice for the computer
    comp_choice = random.choice(choices)
    print(f"Your choice: {user_choice}\nComputer choice: {comp_choice}")

    # Determine the game winner based on standard rules
    if user_choice == comp_choice:
        print("It is a tie!")
    elif user_choice == "rock":
        if comp_choice == "scissor":
            print(f"{user_choice.capitalize()} smashes {comp_choice}. You win!")
        else:
            print(f"{comp_choice.capitalize()} covers {user_choice}. You lose!")
    elif user_choice == "paper":
        if comp_choice == "rock":
            print(f"{user_choice.capitalize()} covers {comp_choice}. You win!")
        else:
            print(f"{comp_choice.capitalize()} cuts {user_choice}. You lose!")
    else:
        if comp_choice == "paper":
            print(f"{user_choice.capitalize()} cuts {comp_choice}. You win!")
        else:
            print(f"{comp_choice.capitalize()} smashes {user_choice}. You lose!")

    # Ask player if they want to continue or exit
    print()
    new_game_choice = ["yes", "no"]
    user_choice = input("Start a new game (yes or no)? ")

    while not user_choice in new_game_choice:
        print("\nInvalid choice!")
        user_choice = input("Start a new game (yes or no)? ")

    if user_choice == "no":
        break

print("\nThanks for playing.")
