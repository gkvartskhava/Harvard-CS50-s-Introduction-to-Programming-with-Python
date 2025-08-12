import re
def main():
    print(convert(input("Hours: ")))
def convert(s):
    match = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if match:
        text = match.groups()
        if int(text[1]) > 12 or int(text[5]) > 12:
            raise ValueError
        time1 = formated_time(text[1],text[2],text[3])
        time2 = formated_time(text[5],text[6],text[7])
        return time1 + ' to ' + time2
    else:
        raise ValueError

def formated_time(hour1,min,amPm):
    if amPm == "PM":
        if int(hour1) == 12:
            hour2 = 12
        else:
            hour2 = int(hour1) + 12
    else:
        if int(hour1) == 12:
            hour2 = 0
        else:
            hour2 = int(hour1)
    if min == None:
        new_minute = ":00"
        new_time = f"{hour2:02}" + new_minute
    else:
        new_time = f"{hour2:02}" + ":" + min

    return new_time

if __name__ == "__main__":
    main()
