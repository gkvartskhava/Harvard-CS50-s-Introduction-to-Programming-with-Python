from twttr import shorten

def main():
    test_cases()
    test_numbers()
    test_comma()

def test_cases():
    assert shorten('george') == 'grg'
    assert shorten('GEORGE') == 'GRG'
    assert shorten('GEOrge') == 'Grg'

def test_numbers():
    assert shorten('12345') == '12345'

def test_comma():
    assert shorten(',./!') == ',./!'


if __name__ == "__main__":
    main()
