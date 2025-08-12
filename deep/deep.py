def main():
    life = input("What is the Answer to the Great Question of Life, the Universe, and Everithing? ")
    answer = life.strip().lower()
    if answer == "42":
        print("Yes")
    elif answer == "forty two":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    else:
        print("No")
main()
