import csv
from tabulate import tabulate
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    input1 = sys.argv[1]

    if '.csv' not in input1:
        sys.exit('Not a Csv file')
    else:
        pizza = open_data(input1)
        print(pizza)

def open_data(input):
    pizza_list = []
    try:
        with open(input,'r') as file:
        #    data = csv.reader(file)
        #    for row in data:
        #        pizza_list.append(row)

            data = csv.DictReader(file)
            for row in data:
                pizza_list.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
        
    #pizza = (tabulate(pizza_list[1:],headers = pizza_list[0],tablefmt="grid"))

    return (tabulate(pizza_list,headers = 'keys',tablefmt="grid"))

if __name__ == "__main__":
    main()
