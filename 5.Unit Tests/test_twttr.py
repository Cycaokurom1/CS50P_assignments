from twttr import shorten


def test_vowel():
    assert shorten('hello') == 'hll'
    assert shorten('lOop') == 'lp'
    assert shorten('Hello, world!') == 'Hll, wrld!'


def test_novowel():
    assert shorten('CS50') == 'CS50'