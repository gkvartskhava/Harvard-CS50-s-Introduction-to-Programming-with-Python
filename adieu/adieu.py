import inflect


def main():
    mylist = []
    while True:
        try:
            p = inflect.engine()
            word = input("Name: ")
            mylist.append(word)
            mylist1 = p.join(mylist)
            new_word = (f"Adieu, adieu, to {mylist1}")

        except EOFError:
            print(new_word)
            break

if __name__ == "__main__":
    main()






