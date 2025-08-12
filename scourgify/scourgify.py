import csv
import sys
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        name = sys.argv[1]
        data = sys.argv[2]
        if '.csv' not in name or 'csv' not in data:
            sys.exit('Not a Csv file')
        else:
            open_data(name,data)
    except FileNotFoundError:
            sys.exit(f"Could not read {name}")
def open_data(input_file, output_file):
    arr = []
    try:
        with open(input_file, 'r') as file:
            data = csv.DictReader(file)
            for row in data:
                full_name = row['name'].split(",")
                new_row = {
                    'first': full_name[1].strip(),
                    'last': full_name[0].strip()
                }
                for key, value in row.items():
                    if key != 'name':
                        new_row[key] = value.strip()
                        arr.append(new_row)
        print(tabulate(arr, headers="keys"))
        with open(output_file, 'w') as file:
            fieldnames = ['first', 'last','house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(arr)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
