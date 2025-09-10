import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r'([0-9]{1,2})(:[0-9][0-9])? (AM|PM) to ([0-9]{1,2})(:[0-9][0-9])? (AM|PM)', s)
    if matches is None:
        raise ValueError
    if int(matches.group(1)) > 12 or int(matches.group(4)) > 12 or int(matches.group(4)) == 0 or int(matches.group(1)) == 0:
        raise ValueError
    for i in [2, 5]:
        if matches.group(i) is not None:
            tmp = matches.group(i).replace(':', '')
            if int(tmp) >= 60:
                raise ValueError

    start_h = hour(matches.group(1), matches.group(3))
    start_m = minute(matches.group(2))
    end_h = hour(matches.group(4), matches.group(6))
    end_m = minute(matches.group(5))

    return f'{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}'


def hour(n, m):
    if m == 'AM':
        if 1 <= int(n) <= 11:
            return int(n)
        elif int(n) == 12:
            return 0
    elif m == 'PM':
        if 1 <= int(n) <= 11:
            return int(n) + 12
        elif int(n) == 12:
            return 12


def minute(n):
    if n is None:
        return 0
    else:
        return int(n.replace(':', ''))


if __name__ == "__main__":
    main()