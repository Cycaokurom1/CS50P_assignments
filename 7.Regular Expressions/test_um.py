from um import count


def test_case():
    assert count('um') == 1
    assert count('Um') == 1
    assert count('uM') == 1
    assert count('UM') == 1


def test_words():
    assert count('yummy') == 0
    assert count('aluminum') == 0
    assert count('cat') == 0


def test_blank():
    assert count(' um ') == 1
    assert count('yummy um') == 1


def test_others():
    assert count('um...') == 1
    assert count('um, hello, um, world') == 2
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1