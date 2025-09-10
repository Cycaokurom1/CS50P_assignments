from working import convert
from pytest import raises


def test_h():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 PM to 6 PM') == '21:00 to 18:00'
    assert convert('12 PM to 5 AM') == '12:00 to 05:00'
    assert convert('12:00 AM to 7:00 PM') == '00:00 to 19:00'
    with raises(ValueError):
        convert('13:00 AM to 11 PM')
        convert('11:42 PM to 0:00 AM')


def test_m():
    assert convert('10:00 AM to 5 PM') == '10:00 to 17:00'
    assert convert('9 AM to 5:45 PM') == '09:00 to 17:45'
    assert convert('1:59 PM to 6 AM') == '13:59 to 06:00'
    with raises(ValueError):
        convert('3:60 AM to 12 PM')


def test_to():
    with raises(ValueError):
        convert('3 AM - 12 PM')
        convert('4:35AM to 8PM')
        convert('7:30 to 12:34')
        convert('9:00 AM - 5:30 PM')
        convert('9: AM - 5: PM')
        convert('10:00 AM - 5 PM')


def test_others():
    with raises(ValueError):
        convert('9 AM - 5:45 PM')
        convert('9 AM 5:45 PM')
        convert('9 AM5:45 PM')
        convert('9 AM  5:45 PM')
        convert('9 AM   5:45 PM')