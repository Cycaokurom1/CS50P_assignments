def main():
    twttr = input('Input: ')

    for i in twttr:
        if isvowel(i):
            twttr = twttr.replace(i, '')

    print('Output:', twttr)


def isvowel(t):
    if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u' or t == 'A' or t == 'E' or t == 'I' or t == 'O' or t == 'U':
        return True
    else:
        return False


main()