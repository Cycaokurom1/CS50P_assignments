def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ## vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False
    ## All vanity plates must start with at least two letters
    elif s[0].isnumeric() or s[1].isnumeric():
        return False
    ## Numbers cannot be used in the middle of a plate; they must come at the end
    elif mid_num(s):
    ##s[-1].isalpha() and (s[3].isnumeric() or s[4].isnumeric() or s[5].isnumeric()):
        return False
    ## The first number used cannot be a '0'
    elif first_zero(s):
        return False
    ## No periods, spaces, or punctuation marks are allowed
    elif s.isalnum():
        return True
    else:
        return False


def mid_num(plate):
    for i in range(2, len(plate)):
        if plate[i].isnumeric():
            for j in range(i, len(plate)):
                if plate[j].isalpha():
                    return True
        return False


def first_zero(plate):
    for p in plate:
        if p.isnumeric() and p != '0':
            return False
        elif p.isnumeric() and p == '0':
            return True
    return False


main()