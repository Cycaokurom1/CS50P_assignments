from seasons import date_validity, get_ordinal, calc_minutes, num_to_words
from datetime import date


def test_ordinal():
    assert get_ordinal('2002-03-11') == (date.today().toordinal(), 730920)


def test_minutes():
    assert calc_minutes(731750, 730920) == 1195200


def test_words():
    assert num_to_words(525600) == 'Five hundred twenty-five thousand, six hundred minutes'
    assert num_to_words(1440) == 'One thousand, four hundred forty minutes'
    assert num_to_words(15778080) == 'Fifteen million, seven hundred seventy-eight thousand eighty minutes'


#get_date无效输入格式
#get_ordinal序号对不对
#calc_minutes算的对不对
#num_to_words转换对不对
