dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total = 0
    while True:
        try:
            user_input = input(f"Item: ").title()
        except EOFError:
            print()
            break
        if user_input in dict:
            total += dict[user_input]
            print(f"Total: ${total:.2f}")

main()


