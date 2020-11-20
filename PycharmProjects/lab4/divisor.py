def greatest_common_divisor():  # funkcja by była bardziej uniwersalna, gdyby przyjmowała liczby jako argumenty
    a = read_positive_number()
    b = read_positive_number()
    while b != 0:
        c = a % b   # c jest niepotrzebne, można to załatwić w jednej linijce
        a, b = b, c
    return a


def read_positive_number():
    a = float(input('Type positive number: '))  # a jak wpiszę "kopytko"?
    while a <= 0:
        a = float(input('It was not a positive number. Try again: '))
    return a
