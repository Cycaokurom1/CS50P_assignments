def main():
    amount = 50
    while amount > 0:
        print('Amount Due:', amount)
        coin = get_coin()
        amount = amount - coin
    amount = 0 - amount
    print('Change Owed:', amount)


def get_coin():
    insert = int(input('Insert Coin: '))
    if insert == 5 or insert == 10 or insert ==25:
        return insert
    else:
        return 0


main()