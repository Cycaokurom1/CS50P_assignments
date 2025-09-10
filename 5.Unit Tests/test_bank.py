from bank import value


def test_hello():
    assert value('hello') == 0


def test_h():
    assert value('ha') == 20


def test_leadingspace():
    assert value('   hello') == 0
    assert value('   heloo') == 20
    assert value('  adnjvca') == 100


def test_caseinsensitively():
    assert value('Hello') == 0
    assert value('HelOo') == 20
    assert value('SFAhjvca') == 100


def test_others():
    assert value('h329iork') == 20
    assert value(',.adw1dsacx31') == 100