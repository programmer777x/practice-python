"""
Practice Python - Exercise 08: Rock Paper Scissors

A local 2-player command-line Rock, Paper, Scissors game.
Includes player name inputs, choice validation, and a replay system.

Exercise URL: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
"""


print()


# Valid options for the game and replay prompts
choices = ["rock", "paper", "scissor"]

# Get names for both players before the game loop starts
user1_name = input("Enter player 1 name: ")
user2_name = input("Enter player 2 name: ")

while True:
    user1_choice = input(f"\n{user1_name}, enter your choice (rock, paper, scissor): ").lower()

    # Validate Player 1's input
    while not user1_choice in choices:
        print("\nInvalid choice!")
        user1_choice = input(f"{user1_name}, enter your choice (rock, paper, scissor): ").lower()

    user2_choice = input(f"{user2_name}, enter your choice (rock, paper, scissor): ").lower()

    # Validate Player 2's input
    while not user2_choice in choices:
        print("\nInvalid choice!")
        user2_choice = input(f"{user2_name}, enter your choice (rock, paper, scissor): ").lower()
    print()

    print(f"{user1_name}'s choice: {user1_choice}\n{user2_name}'s choice: {user2_choice}")

    # Determine the game winner based on standard rules
    if user1_choice == user2_choice:
        print("It is a tie!")
    elif user1_choice == "rock":
        if user2_choice == "scissor":
            print(f"{user1_choice.capitalize()} smashes {user2_choice}. {user1_name} win!")
        else:
            print(f"{user2_choice.capitalize()} covers {user1_choice}. {user2_name} win!")
    elif user1_choice == "paper":
        if user2_choice == "rock":
            print(f"{user1_choice.capitalize()} covers {user2_choice}. {user1_name} win!")
        else:
            print(f"{user2_choice.capitalize()} cuts {user1_choice}. {user2_name} win!")
    else:
        if user2_choice == "paper":
            print(f"{user1_choice.capitalize()} cuts {user2_choice}. {user1_name} win!")
        else:
            print(f"{user2_choice.capitalize()} smashes {user1_choice}. {user2_name} win!")

    # Ask player if they want to continue or exit
    print()
    new_game_choice = ["yes", "no"]
    new_game = input("Start a new game (yes or no)? ")

    while not new_game in new_game_choice:
        print("\nInvalid choice!")
        new_game = input("Start a new game (yes or no)? ")

    if new_game == "no":
        break

print("\nThanks for playing.")
