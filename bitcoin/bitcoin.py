import requests
import sys

def main():
    url = f"https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    r = response.json()

    try:

        if len(sys.argv) <= 1:
            sys.exit("Missing command-line argument")

        try:
            sys.argv[1] = float(sys.argv[1])

        except ValueError:
            sys.exit("Command-line argument is not a number")

        rate = r["bpi"]["USD"]["rate_float"]
        rate = rate
        number = float(sys.argv[1])
        amount = rate * number
        print(f"${amount:,.4f}")
    except requests.RequestException:
        print("RequestException")
        sys.exit(1)

if __name__ == "__main__":
    main()

