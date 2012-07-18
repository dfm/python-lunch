import numpy as np
import scipy.optimize as op
import emcee

import line

# Read in the data file.
data = np.array([l.split() for l in open("../data.dat")], dtype=float)

# Initial guess.
p0 = np.array([1.0, 1.0])


def optimize():
    chi2 = lambda p: -2 * line.lnlike(p, data)
    p = op.fmin(chi2, p0)
    print p


if __name__ == "__main__":
    optimize()
