from fuel import convert, gauge
from pytest import raises


def test_convert():
    assert convert('3/4') == 75
    assert convert('2/3') == 67
    with raises(ValueError):
        convert('1.5/4')
        convert('1/4.45')
        convert('5/4')
    with raises(ZeroDivisionError):
        convert('1/0')


def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'