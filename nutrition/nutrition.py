def main():
    table = {
        "apple" : 130,
        "avocado": 50,
        "sweet cherries":100,
        "banana":110,
        "kiwifruit":90,
        "pear":100
    }
    food = input("Item: ").lower()
    for i in table:
         if food == i:
            print("Calories:",table[i])

main()
