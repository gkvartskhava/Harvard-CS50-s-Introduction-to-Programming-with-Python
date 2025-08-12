#n breakfast time, lunch time, or dinner time
def main():
    word = input("What time is it? ")
    new_word = convert(word)
    if new_word >= 7 and new_word <= 8:
        print("breakfast time")
    elif new_word >=12 and new_word <= 13:
        print("lunch time")
    elif new_word >= 18 and new_word<= 19:
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    minutes1 = float(minutes) / 60
    return float(hours) + minutes1

if __name__ == "__main__":
    main()
