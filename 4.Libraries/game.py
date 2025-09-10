import random
import sys


def main():
    level = check_input('Level: ')
    target = random.randint(1, level)
    while True:
        guess = check_input('Guess: ')
        if guess > target:
            print('Too large!')
        elif guess < target:
            print('Too small!')
        elif guess == target:
            sys.exit('Just right!')


def check_input(prompt):
    while True:
        i = input(prompt)
        if i.isdecimal() and int(i) > 0:
            return int(i)


main()