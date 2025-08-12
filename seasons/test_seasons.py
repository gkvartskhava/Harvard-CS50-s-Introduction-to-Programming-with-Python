from seasons import answer

def test_answer():
    assert answer(1999,1,1) == 'Thirteen million, three hundred eighty-nine thousand, one hundred twenty minutes'
    assert answer(1992,9,1) == 'Sixteen million, seven hundred nineteen thousand, eight hundred forty minutes'
    assert answer(2000,9,1) == 'Twelve million, five hundred twelve thousand, one hundred sixty minutes'
