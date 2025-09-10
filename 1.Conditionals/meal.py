def main():
    t = input('What time is it? ')
    x = convert(t)
    if 7.0 <= x <= 8.0:
        print('breakfast time')
    elif 12.0 <= x <= 13.0:
        print('lunch time')
    elif 18.0 <= x <= 19.0:
        print('dinner time')


def convert(time):
    if time.endswith('p.m.'):
        h, m = time.removesuffix(' p.m.').split(':')
        y = 12 + float(h) + float(m) / 60
    elif time.endswith('a.m.'):
        h, m = time.removesuffix(' a.m.').split(':')
        y = float(h) + float(m) / 60
    else:
        h, m = time.split(':')
        y = float(h) + float(m) / 60
    return y


if __name__ == "__main__":
    main()