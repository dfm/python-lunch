import numpy as np
import scipy.optimize as op
import emcee

import matplotlib.pyplot as pl

import line

# Read in the data file.
data = np.array([l.split() for l in open("../data.dat")], dtype=float)
m_true, b_true = np.array(open("../truth.dat").read().split(), dtype=float)


def optimize():
    # Do the optimization.
    pass


def sample():
    pass


if __name__ == "__main__":
    print "Optimizing..."
    optimize()
    print

    print "Sampling..."
    sample()
    print
