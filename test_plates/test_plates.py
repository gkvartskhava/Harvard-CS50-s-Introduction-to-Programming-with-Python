from plates import is_valid

def testlength():
    assert is_valid('qq') == True
    assert is_valid('') == False
    assert is_valid('asdasdasdsd') == False
    assert is_valid('2313123131') == False

def testmiddle():
    assert is_valid('qq111qq') == False
    assert is_valid('0qqss') == False
    assert is_valid('cs50') == True
    assert is_valid('aa>!ww') == False
    assert is_valid('aa>.,:') == False
def test_digits():
    assert is_valid('111qq') == False
    assert is_valid('q') == False
    assert is_valid('1') == False

def test_alpha():
    assert is_valid('qqqqq') == True
    assert is_valid('as5gh') == False
def test_plate():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('55') == False
    assert is_valid('AAa012') == False
