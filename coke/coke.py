def main():
    total = 50
    while total > 0:
        print(f"Amount Due: {total}")
        sum = int(input("Insert coin: "))
        if sum == 25 or sum == 10 or sum == 5:
            total -= sum
        else:
            print(f"Invalid coin")
    else:
        change = abs(total)
        print(f"Change Owed: {change}")
main()


