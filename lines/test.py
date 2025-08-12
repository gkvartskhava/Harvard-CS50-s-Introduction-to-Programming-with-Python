import pytest
from lines import open_file


def test_lines():
    assert open_file('testhello.py') == 2
    with pytest.raises(FileNotFoundError):
        open_file('hell.py')
