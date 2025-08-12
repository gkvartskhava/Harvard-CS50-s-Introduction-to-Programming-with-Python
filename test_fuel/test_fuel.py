import pytest
from fuel import gauge,convert


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')
        convert('4/0')
        convert('1/0')

def test_convertt():
    assert convert('1/100') == 1
    assert convert('3/4') == 75
    assert convert('99/100') == 99

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(75) == '75%'
    assert gauge(1) == 'E'

def testValue():
    with pytest.raises(ValueError):
        convert('apple/tree')
        convert('car/treat')
        convert('road/house')
