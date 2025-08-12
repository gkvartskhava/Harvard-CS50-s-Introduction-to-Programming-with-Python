def main():
    greeting = input("Greeting: ").lower().strip()
    word = bank(greeting)
    print(f"{word}")
def bank(x):
    if x.startswith("hello"):
        return "$0"
    elif x.startswith("h") and not x.startswith("hello"):
        return("$20")
    else:
        return "$100"
main()
