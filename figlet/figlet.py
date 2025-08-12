from pyfiglet import Figlet
import sys

def main():

    try:
        figlet = Figlet()
        all_fonts = figlet.getFonts()


        if len(sys.argv) == 1:
            word = input("Input: ")
            new_word = figlet.renderText(word)
            print(new_word)

        elif len(sys.argv) > 1 and (sys.argv[1] == "-f" or sys.argv[1] == "--f"):
            style = sys.argv[2]
            if style in all_fonts:
                figlet.setFont(font=style)
                word = input("input: ")
                new_word = figlet.renderText(word)
                print(new_word)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    except Exception:
        sys.exit("Invalid usage")
if __name__ == "__main__":
    main()
