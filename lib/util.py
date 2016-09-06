from os import path
import inspect


def realpath(filename):
    from_dir = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
    return path.abspath(path.join(from_dir, filename))


def round_to_tens(number):
    if hasattr(number, '__iter__'):
        number = map(round_to_tens, number)
    else:
        diff = number % 10
        if diff >= 5:
            number += (10 - diff)
        else:
            number -= diff

    return number


