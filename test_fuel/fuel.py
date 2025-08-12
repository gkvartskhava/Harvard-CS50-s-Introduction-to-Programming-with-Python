def main():
    user_input = input('Fraction: ')
    fraction = convert(user_input)
    answer = gauge(fraction)
    print(answer)

def convert(fraction):
        while True:
             try:
                    x, y = map(int, fraction.split("/"))
                    fuel = x / y
                    if fuel <= 1:
                        percent = int(fuel * 100)
                        return percent

                    else:
                       fraction = input('Fraction: ')
                       pass

             except (ValueError,ZeroDivisionError):
                    raise

def gauge(percentage):
    if percentage <= 1:
         return "E"
    elif percentage >= 99:
         return "F"
    else:
         p = str(percentage)
         return f'{p}%'

if __name__ == "__main__":
    main()
