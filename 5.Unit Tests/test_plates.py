from plates import is_valid


def test_twoletters():
    assert is_valid('X5050') == False
    assert is_valid('50CS') == False


def test_length():
    assert is_valid('A') == False
    assert is_valid('ASDFGGH') == False


def test_midnumber():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False


def test_firstnumber():
    assert is_valid('AAA022') == False


def test_punctuation():
    assert is_valid('AA.022') == False
    assert is_valid('AA 222') == False
    assert is_valid('AA??22') == False
