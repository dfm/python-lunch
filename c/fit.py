import numpy as np
import scipy.optimize as op
import emcee

import matplotlib.pyplot as pl

import line

# Read in the data file.
data = np.array([l.split() for l in open("../data.dat")], dtype=float)
m_true, b_true = np.array(open("../truth.dat").read().split(), dtype=float)

# Initial guess.
p0 = np.array([1.0, 1.0])


def optimize():
    chi2 = lambda p: -2 * line.lnlike(p, data)
    p = op.fmin(chi2, p0)
    return p


def plot(p):
    pl.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt="ok")
    x = np.array([0, 5])
    pl.plot(x, m_true * x + b_true, "--k", lw=2.0)
    pl.plot(x, p[0] * x + p[1], "r", lw=2.0)

    pl.title(r"truth: $(%.1f, %.1f)$, fit: $(%.3f, %.3f)$"
            % (m_true, b_true, p[0], p[1]))

    pl.xlabel("$x$")
    pl.ylabel("$y$")


if __name__ == "__main__":
    p = optimize()
    plot(p)
    pl.savefig("optimize.png")
