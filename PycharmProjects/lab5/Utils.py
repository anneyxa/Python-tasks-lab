import re

from Program import *


def check_name_exists(name, names):
    if name in names:
        return name
    else:
        raise ValueError(f'There is no figure named: {name}.')


def validate_name(name):
    if name[0].isdigit():
        raise ValueError('Name cannot start with a digit.')
    name_regex = re.compile('[a-zA-Z0-9_]+')
    if name_regex.fullmatch(name):
        return name
    else:
        raise ValueError(f'Name: {name} is not a valid name. Use only letters, numbers or underlines.')


def check_size_number(size):
    for index, val in enumerate(size):
        size[index] = float(val)
    return size


def validate_size_expected(size, expected):
    if len(size) != expected:
        raise ValueError(f'Expected number of size args: {expected}, received: {len(size)}')
    return size


def validate_ratio(ratio):
    if ratio.isnumeric() and ratio != 0:    # przekazuje Pani stringa do tej funkcji, więc drugi warunek zawsze jest spełniony ("0" != 0) - najpierw trzeba przekonwertować
        return int(ratio)
    else:
        raise ValueError('Ratio must be a non-zero number.')


def validate_angle(angle):
    if angle.isnumeric():
        return angle
    else:
        raise ValueError('Angle must be a number.')

