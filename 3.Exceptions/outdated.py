months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ')
    try:
        if '/' in date:
            m, d, y = date.split('/')
            if 0 <= int(m) <= 11 and 1 <= int(d) <= 31:
                print(f'{int(y)}-{int(m):02}-{int(d):02}')
                break
            else:
                pass
        elif ',' in date:
            mm, dd, y = date.split()
            m = months.index(mm)
            d = dd.replace(',', '')
            if 0 <= int(m) <= 11 and 1 <= int(d) <= 31:
                print(f'{int(y)}-{int(m) + 1:02}-{int(d):02}')
                break
            else:
                pass
    except ValueError:
        pass