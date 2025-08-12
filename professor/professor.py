import random

def main():
    level = get_level()
    correct = game(level)

    print(f"Score:",correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x,y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x,y
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x,y

def ask_question(x, y):
    z = x + y
    attempts = 1

    while attempts <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == z:
                return True
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("EEE")
            attempts += 1

    print(f"{x} + {y} = {z}")
    return False

def game(level):
    tries = 1
    correct = 0
    while tries <=10:
        x,y = generate_integer(level)
        answer = ask_question(x, y)
        if answer == True:
            correct += 1
        tries += 1
    return correct

if __name__ == "__main__":
    main()

