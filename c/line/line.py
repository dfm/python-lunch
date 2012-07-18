__all__ = ["lnlike"]


import _line


def lnlike(p, data):
    return _line.lnlike(p[0], p[1], data[:, 0], data[:, 1], data[:, 2])
