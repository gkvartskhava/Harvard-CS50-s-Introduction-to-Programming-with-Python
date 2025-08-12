import re
import sys

def main():
    print(parse(input("HTML: ")))
def parse(s):
    x = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+)"',s)
    if x:
        link = 'https://youtu.be/' + x.group(1)
        return link
if __name__ == "__main__":
    main()
