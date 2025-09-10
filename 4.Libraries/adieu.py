names = []

while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        if len(names) == 1:
            print('Adieu, adieu, to', names[0])
            break
        elif len(names) == 2:
            print('Adieu, adieu, to', names[0], 'and', names[1])
            break
        else:
            print('Adieu, adieu, to ', end='')
            for i in names[0:-1]:
                print(f'{i}, ', end='')
            print('and', names[-1])
            break

