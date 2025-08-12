list = [
    "January","February","March","April","May","June","July","August","September","October","November",
    "December" ]

def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month, day, year = map(int, date.split("/"))
            elif "," in date:
                month2, day, year = date.replace(",", "").split()
                month = list.index(month2) + 1
                day = int(day)
                year = int(year)
            else:
                continue

            if not (1 <= month <= 12 and 1 <= day <= 31):
                continue

            break
        except (ValueError, IndexError):
            continue

    print(f"{year}-{month:02}-{day:02}")

main()
