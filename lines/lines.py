import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    text = sys.argv[1]
    if text[-3:] != '.py':
        sys.exit('Not a Python file')
    elif text[-3:] == '.py':
        length = open_file(text)
        print(length)

def open_file(file_path):
    try:
        with open(file_path,"r") as file:
            lines = 0
            for e in file:
                if not e.lstrip().startswith('#') and e.lstrip() != "":
                    lines += 1
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

