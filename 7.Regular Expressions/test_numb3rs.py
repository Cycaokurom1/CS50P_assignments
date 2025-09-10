from numb3rs import validate


def test_range():
    assert validate('1.2.3.4') == True
    assert validate('0.255.0.255') == True
    assert validate('1.12.123.1234') == False
    assert validate('-1,0,1,2') == False
    assert validate('9.876.54.32') == False
    assert validate('98.76.543.21') == False


def test_dot():
    assert validate('1.2.4.8') == True
    assert validate('1.2.3') == False
    assert validate('1.2.3.4.5') == False
    assert validate('123') == False


def test_others():
    assert validate('cat') == False
    assert validate('a.b.c.d') == False
    assert validate(' 4. 2.3.4') == False
    assert validate('_=?') == False