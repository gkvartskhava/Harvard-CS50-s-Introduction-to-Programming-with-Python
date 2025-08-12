from numb3rs import validate


def test_validate_true():
    assert validate('89.255.120.180') == True
    assert validate('23.245.70.50') == True
    assert validate('90.255.20.10') == True
    assert validate('100.255.255.255') == True

def test_validate_false():
    assert validate('10.10.10.10.10') == False
    assert validate('1.555.555.555') == False
    assert validate('cat') == False
    assert validate('dog') == False

