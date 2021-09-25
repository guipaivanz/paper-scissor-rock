import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def score():
    print(f"Computer wins: {computer_win_count}")
    print(f"{user_name} wins: {user_win_count}")


clear()
print("Let's play Paper Scissors Rock. Can you beat me?")
user_name = input("First, please enter your name: ")
game_choices = ['p', 's', 'r']
print(f"\nHello {user_name}. Lets battle!!\n")

user_win_count = 0
computer_win_count = 0
exit_game = False
while exit_game != True:
    print("Score:")
    score()
    print("\nChoose one of the following or press 'ENTER' for a random choise")
    print("Paper: 'p'\nScissors: 's'\nRock: 'r'\n")
    user_choice = input("p, s, r or ENTER for random: ")

    if len(user_choice) == 0:
        user_choice = random.choice(game_choices)
    else:
        user_choice = user_choice.lower()
    computer_choice = random.choice(game_choices)
    print(user_choice)
    if user_choice == "p" and computer_choice == "r" or user_choice == "r" and computer_choice == "s" or user_choice == "s" and computer_choice == "p":
        print("You win!! :-)")
        user_win_count = user_win_count + 1
    elif user_choice == computer_choice:
        print("It is a tie!! :-|")
    else:
        print("You lost!! :-(")
        computer_win_count = computer_win_count + 1

    exit_game_option = input(
        "Type 'Yes' to exit game or 'ENTER' to continue: ").lower()
    if exit_game_option == "yes":
        exit_game = True
    else:
        exit_game = False
        clear()

if user_win_count > computer_win_count:
    print("\nYou are the WINNER")
else:
    print("\nBetter luck next time.")
print("Here is the final score:")
score()
