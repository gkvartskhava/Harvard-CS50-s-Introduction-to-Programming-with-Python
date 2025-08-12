import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    answer = re.findall(r'\b(um)\b',s,re.IGNORECASE)
    return len(answer)

if __name__ == "__main__":
    main()






