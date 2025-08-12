from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.__init__(-1)
        jar.__init__(-5)
        jar.__init__(-20)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(14)
        jar.deposit(20)
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
        jar.withdraw(15)
        jar.withdraw(20)
