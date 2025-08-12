
def main():
    name = input("name: ")
    for element in name:
        if element.isupper():
            print("_"+element.lower(), end="")
        else:
            print(element,end="")
    print()
# firstName = input("firstName: ")
# preferredFirstName = input("preferredFirstName: ")

main()

