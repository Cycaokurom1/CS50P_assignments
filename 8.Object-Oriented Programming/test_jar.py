from jar import Jar
from pytest import raises


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    '''
    with raises(ValueError):
        jar.capacity = -1
        jar.capacity = '🍪'
    '''


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    with raises(ValueError):
        jar.deposit(13)
        jar.deposit('🍪')


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with raises(ValueError):
        jar.withdraw(13)
