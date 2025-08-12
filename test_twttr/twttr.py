import sys

def main():
    try:
        word = input("Input: ")
        shorten_word = shorten(word)
        print(f'Output: {shorten_word}')
    except Exception:
        sys.exit(1)

def shorten(word):
    try:
        new_word = ''
        for e in word:
            if e.lower() not in ["a","e","i","o","u",]:
                new_word += e

        return new_word
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()

