import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        z = x + y
        chance = 3
        while True:
            try :
                answer = int(input(f'{x} + {y} = '))
                if answer == z:
                    score += 1
                    break
                elif answer != z:
                    chance -= 1
                    print('EEE')
            except ValueError:
                chance -= 1
                print('EEE')
                pass
            if chance == 0:
                print(f'{x} + {y} = {z}')
                break
    print(f'Score: {score}')


def get_level():
    while True:
        level = input('Level: ')
        try:
            if int(level) == 1 or int(level) == 2 or int(level) == 3:
                return(int(level))
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return(random.randint(0,9))
    elif level == 2:
        return(random.randint(10,99))
    elif level == 3:
        return(random.randint(100,999))


if __name__ == "__main__":
    main()