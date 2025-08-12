import emoji

def main():
    x = input("Input: ")
    y = emoji.emojize(x, language='alias')
    print(y)

if __name__ == "__main__":
    main()

