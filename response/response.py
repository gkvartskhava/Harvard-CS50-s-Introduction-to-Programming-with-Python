from validator_collection import checkers

def main():
    email = input(f"What's your email adress: ")
    if validate(email) == True:
        print('Valid')
    elif validate(email) == False:
        print('Invalid')

def validate(s):
    try:
        valid = checkers.is_email(s)
        if valid:
            return True
        else:
            return False
    except Exception:
        return False
if __name__ == "__main__":
    main()
