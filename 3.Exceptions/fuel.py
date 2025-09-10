def main():
    while True:
        f = get_fraction()
        if f <= 1:
            print('E')
            break
        elif f == 99 or f == 100:
            print('F')
            break
        elif 2 <= f <= 98:
            print(f'{int(f)}%')
            break


def get_fraction():
    while True:
        try:
            x, y = input('Fraction: ').split('/')
            return round(100 * int(x) / int(y))
        except (ValueError, ZeroDivisionError):
            pass


main()