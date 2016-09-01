from os import path
import inspect


def realpath(filename):
    from_dir = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))
    return path.abspath(path.join(from_dir, filename))
