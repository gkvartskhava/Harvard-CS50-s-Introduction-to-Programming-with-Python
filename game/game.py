import random

def main():
    try:
        level = int(input("Level: "))
        game_level = gen_number(level)
        while True:
            guess = int(input('Guess: '))
            if guess == 0 or guess < 0:
                continue
            elif guess > game_level:
                print('Too large!')
            elif guess < game_level:
                print("Too small!")
            elif guess == game_level:
                print('Just right!')
                break

    except ValueError:
        main()

def gen_number(n):
    level = random.randint(1, n)
    return level

if __name__ == "__main__":
    main()
