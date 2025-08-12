dict = { }

def main():
    while True:

        try:
            item = input("").lower()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        except EOFError:
            for e in sorted(dict.keys()):
                print(dict[e],e.upper())

            break


main()
