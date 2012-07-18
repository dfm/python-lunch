__all__ = ["lnlike"]


import numpy as np


def lnlike(p, data):
    m, b = p
    chi2 = np.sum(((data[:, 1] - (m * data[:, 0] + b)) / data[:, 2]) ** 2)
    return -0.5 * chi2
