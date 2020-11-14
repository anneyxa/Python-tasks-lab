def greatest_common_divisor():
    a = read_positive_number()
    b = read_positive_number()
    while b != 0:
        c = a % b
        a, b = b, c
    return a


def read_positive_number():
    a = float(input('Type positive number: '))
    while a <= 0:
        a = float(input('It was not a positive number. Try again: '))
    return a
