from working import convert
import pytest

def test_convert():
        with pytest.raises(ValueError):
            convert('9 AM - 9 PM')
        with pytest.raises(ValueError):
            convert('13 PM to 17 PM')
        with pytest.raises(ValueError):
            convert('9:60 AM to 9:60 PM')
        with pytest.raises(ValueError):
            convert("09:00 to 17:00")
        with pytest.raises(ValueError):
            convert(" to ")
        with pytest.raises(ValueError):
            convert("14:00 AM to 13:00 PM")
        with pytest.raises(ValueError):
            convert("0:00 AM to 0:00 PM")
        with pytest.raises(ValueError):
            convert("13 AM to 15 PM")
        with pytest.raises(ValueError):
            convert("0 AM to 0 PM")
        with pytest.raises(ValueError):
            convert("13:67 AM to 7:61 PM")
        with pytest.raises(ValueError):
            convert("9AM to 5PM")
        with pytest.raises(ValueError):
            convert("6:19 AM 4:20 PM")
def test_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("10:30 PM to 8:30 AM") == "22:30 to 08:30"
