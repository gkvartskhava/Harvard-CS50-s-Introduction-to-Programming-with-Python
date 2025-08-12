# Rock, Paper, Scissors & Sheldon's Game

![Language](https://img.shields.io/badge/language-python-blue)
![Module](https://img.shields.io/badge/module-random-orange)

## About
This project is developed as final project for Harvard University's CS50x Introduction to Computer Science Course, in June
2024.
There are implemented two simple games using **Python** and **Random** Library.
Main idea of the project is inspired from 'Big Bang Theory' so called "Sheldon's Game".

**You may find the video demo of the project <a href="https://youtu.be/zJonXFwMPYk">here</a>.**

## Features

- User has to choose which game he/she wants to play by entering '1' or '2'.
   - 1. Classic Rock, Paper, Scissors game
   - 2. Advanced Rock, Paper, Scissors, Lizard, Spock game (Sheldon's game)
- If User's input is not valid it repeats question until valid input is entered.
- Game continues until a player reaches 3 points
- Exit the game at any moment by pressing `Ctrl + D` or `Ctrl + C`

## Introduction and Overview
This project offers two interactive games for users to enjoy:

1. **Standart Rock, Paper, Scissors:** The classic game where each player simultaneously forms one of three shapes with an
outstretched hand. These shapes are "rock", "paper", and "scissors". Each shape beats one of the other shapes: rock
crushes scissors, scissors cuts paper, and paper covers rock.
2. **Sheldon's Game:** An advanced version of the classic game, including two additional choices: "lizard" and "Spock".
This version is popularized by the TV show "The Big Bang Theory" and adds complexity and fun to the traditional game. The
additional rules are:
   - Rock crushes Scissors
   - Scissors cuts Paper
   - Paper covers Rock
   - Rock crushes Lizard
   - Lizard poisons Spock
   - Spock smashes Scissors
   - Scissors decapitates Lizard
   - Lizard eats Paper
   - Paper disproves Spock
   - Spock vaporizes Rock

Players compete against the computer, and the game continues until one player reaches 3 points.
'''
score1 = 0
score2 = 0
while score1 < 3 and score2 < 3:
'''

The player can choose to exit the game at any moment by pressing `Ctrl + D` or `Ctrl + C`.

'''
except (EOFError,KeyboardInterrupt):
        print()
        sys.exit("Have a nice day")
'''
Special thanks to Harvard University, Prof. David J. Malan, and the staff!


## Usage
To start the game, run the following command in your terminal:
```bash
python project.py



