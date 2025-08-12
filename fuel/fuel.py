def main():
    while True:
        user_input = input("Fraction: ")
        try:
            x, y = map(int, user_input.split("/"))
            if y == 0 or x > y:
                continue
            z = round(x / y * 100)
            if z <= 1:
                print("E")
            elif z >= 99:
                print("F")
            else:
                print(f"{z}%")
            break
        except (ValueError, ZeroDivisionError):
            continue

main()
