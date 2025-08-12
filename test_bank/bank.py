def main():
    s: str = input("Greeting: ")
    s = s.lower().strip()
    print(value(s))
def value(greeting: str):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
if __name__ == "__main__":
    main()


