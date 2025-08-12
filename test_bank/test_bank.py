from bank import value
def test_value():
    assert value("Hello") == 0
    assert value("How are you doing tomorrow?") == 20
    assert value("What's for today?") == 100
    assert value("What's up?") == 100



