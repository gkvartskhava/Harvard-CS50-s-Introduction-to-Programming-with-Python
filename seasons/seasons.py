from datetime import date
import inflect
import sys
p = inflect.engine()
def main():
    try:
        user_date = input('Date of Birth: ')
        year,month,day = map(int, user_date.split("-"))
    except ValueError:
            sys.exit('Invalid Date')

    print(answer(year,month,day))


def answer(year,month,day):
     try:
         time = date(year,month,day)
     except ValueError:
        return 'Invalid Date'
     today = date.today()
     total = today - time
     minutes = int(total.total_seconds() / 60)
     word = p.number_to_words(minutes, andword="")+' minutes'
     return word.capitalize()
if __name__ == "__main__":
    main()




