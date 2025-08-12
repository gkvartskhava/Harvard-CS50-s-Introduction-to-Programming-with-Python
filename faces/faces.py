def main():
    x = input()
    result = smile(x)
    print(result)


def smile(x):
    z = x.replace(":)","🙂")
    y = z.replace(":(","🙁")
    return y


main()





