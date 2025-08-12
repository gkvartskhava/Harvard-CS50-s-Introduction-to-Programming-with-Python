import random
import sys

def main():
    global list_choices,list_choices2

    # Define choices for both games
    list_choices = ['rock','paper','scissors']
    list_choices2 = ['rock','paper','scissors','lizard','spock']

    # Display game instructions and options
    print(f'Here are 2 games, game continues till 3 points, you can exit game any moment by pushing "ctrl + d" ')
    print(f'Choose what game you want to play: "1" or "2" ')
    print(f'1. Rock, Paper, Scissors.')
    print(f"2. Sheldon's game.")

    # Get user input for game choice
    user_input = check_input()
    advanced = game(user_input)
    print(advanced)

def check_input():
    try:
        while True:
            user_input = input("your choice: ")
            if user_input == '1' or user_input == '2':
                return user_input
            else:
                print("Choose either '1' or '2'")
                continue
    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")

def random_choice(list):
    # Select a random choice from the provided list
    computer_choice = random.choice(list)
    return computer_choice

def game(input2):
    try:
        if input2 == '1':
            # Initialize scores for classic game
            score1 = 0
            score2 = 0
            while score1 < 3 and score2 < 3:
                user_choice = get_user_choice()
                computer_choice = random_choice(list_choices)
                answer,score1,score2 = standart_game(user_choice,computer_choice,score1,score2)
                print(answer)
            # Determine winner
            if score1 > score2:
                return f'You win: {score1} - {score2}.'
            elif score2 > score1:
                return f'Game Over. You lose: {score1} - {score2}.'

        elif input2 == '2':
            # Initialize scores for Sheldon's game
            score1 = 0
            score2 = 0
            while score1 < 3 and score2 < 3:
                user_choice = get_user_choice2()
                computer_choice = random_choice(list_choices2)
                answer,score1,score2 = sheldon_game(user_choice,computer_choice,score1, score2)
                print(answer)
            if score1 > score2:
                return f'You win: {score1} - {score2}.'
            elif score2 > score1:
                return f'Game Over. You lose: {score1} - {score2}.'
        else:
            print("Something went wrong...")
    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")

def standart_game(user_choice,computer_choice,score1,score2):

    try:
        if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            score1 += 1
            return f'Your choice: {user_choice} beats Computer choice: {computer_choice}, +1 point for you !!!', score1, score2
        elif (computer_choice == "rock" and user_choice == "scissors") or \
            (computer_choice == "paper" and user_choice == "rock") or \
            (computer_choice == "scissors" and user_choice == "paper"):
            score2 += 1
            return f'Computer choice: {computer_choice} beats Your choice: {user_choice}, +1 point for computer !!!', score1, score2
        else:
            return "It's a tie...", score1, score2

    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")
def sheldon_game(user_choice,computer_choice,score1, score2):
    # Define the winning cases for Sheldon's game
    winning_cases = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    try:
        if computer_choice in winning_cases[user_choice]:
            score1 += 1
            return f'Your choice: {user_choice} beats Computer choise: {computer_choice}, +1 point for you !!!', score1, score2
        elif user_choice in winning_cases[computer_choice]:
            score2 += 1
            return f'Computer choice: {computer_choice} beats Your choice: {user_choice}, +1 point for computer !!!', score1, score2
        else:
            return "It's a tie...", score1, score2
    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")
def get_user_choice():
    try:
        user_choice = input("choose one from: rock, paper, scissors: ").lower()
        while user_choice not in list_choices:
            print("Invalid choice. Please try again.")
            user_choice = input("choose one from: rock, paper, scissors: ").lower()
        return user_choice
    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")

def get_user_choice2():
    try:
        user_choice = input("choose one from: rock, paper, scissors, lizard, spock: ").lower()
        while user_choice not in list_choices2:
            print("Invalid choice. Please try again.")
            user_choice = input("choose one from: rock, paper, scissors, lizard, spock: ").lower()
        return user_choice
    except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")
if __name__ == "__main__":
    main()
