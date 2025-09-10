from datetime import date
import sys
import re
import inflect


def main():
    birthday = date_validity(input('Date of Birth:'))
    today_ordinal, birthday_ordinal = get_ordinal(birthday)
    minutes = calc_minutes(today_ordinal, birthday_ordinal)
    print(num_to_words(minutes))


def date_validity(date):
    if not re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', date):
        sys.exit('Invalid date')
    return date


def get_ordinal(d):
    return date.today().toordinal(), date.fromisoformat(d).toordinal()


def calc_minutes(t, b):
    return 1440 * (t-b)


def num_to_words(n):
    words = inflect.engine().number_to_words(n)
    words_withand = words.capitalize() + ' minutes'
    return words_withand.replace(' and', '')


#输入符合格式的日期，不符合则sys.exit('Invalid date')
#获得输入日期的ordinal
#根据两个日期的ordinal计算分钟数
#将分钟数转化为英文字符输出，借助hint里面提到的inflect


if __name__ == "__main__":
    main()