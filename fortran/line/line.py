__all__ = ["lnlike"]


import _line


def lnlike(p, data):
    return -0.5 * _line.chi2(p[0], p[1], data[:, 0], data[:, 1], data[:, 2],
            data.shape[0])
