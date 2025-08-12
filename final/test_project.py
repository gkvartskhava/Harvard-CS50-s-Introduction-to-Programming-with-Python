from project import random_choice,standart_game,sheldon_game

def test_random_choice():
    assert random_choice(['spock']) == 'spock'
    assert random_choice(['rock']) == 'rock'
    assert random_choice(['paper']) == 'paper'
    assert random_choice(['dog']) == 'dog'
    assert random_choice(['cat']) == 'cat'

def test_standart_game():
    assert standart_game('rock','scissors',0,0) == ('Your choice: rock beats Computer choice: scissors, +1 point for you !!!',1,0)
    assert standart_game('paper','rock',0,0) == ('Your choice: paper beats Computer choice: rock, +1 point for you !!!',1,0)
    assert standart_game('scissors','paper',0,0) == ('Your choice: scissors beats Computer choice: paper, +1 point for you !!!',1,0)
    assert standart_game('rock','paper',0,0) == ('Computer choice: paper beats Your choice: rock, +1 point for computer !!!',0,1)
    assert standart_game('scissors','rock',0,0) == ('Computer choice: rock beats Your choice: scissors, +1 point for computer !!!',0,1)
    assert standart_game('rock','rock',0,0) == ("It's a tie...",0,0)

def test_sheldon_game():
    assert sheldon_game('rock',"lizard",0,0) == ('Your choice: rock beats Computer choise: lizard, +1 point for you !!!',1,0)
    assert sheldon_game('lizard',"spock",0,0) == ('Your choice: lizard beats Computer choise: spock, +1 point for you !!!',1,0)
    assert sheldon_game('spock',"rock",0,0) == ('Your choice: spock beats Computer choise: rock, +1 point for you !!!',1,0)
    assert sheldon_game('rock',"scissors",0,0) == ('Your choice: rock beats Computer choise: scissors, +1 point for you !!!',1,0)
    assert sheldon_game('spock','spock',0,0) == ("It's a tie...",0,0)
