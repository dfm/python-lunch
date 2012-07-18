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
    # The chi-squared function.
    chi2 = lambda p: -2 * line.lnlike(p, data)

    # Optimize by minimizing chi-squared. This is equivalent to maximizing
    # the likelihood.
    p = op.fmin(chi2, p0)

    # Generate the plot.
    pl.clf()

    # Plot the truth as a dashed black line.
    x = np.array([0, 5])
    pl.plot(x, m_true * x + b_true, "--k", lw=2.0)

    # Plot the fit as a red line.
    pl.plot(x, p[0] * x + p[1], "r", lw=2.0)

    # Over plot the data.
    pl.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt="ok")

    # Show the results in the title.
    pl.title(r"truth: $(%.1f, %.1f)$, fit: $(%.3f, %.3f)$"
            % (m_true, b_true, p[0], p[1]))

    # Save it.
    pl.savefig("optimize.png")


def sample():
    # We'll sample with 100 walkers.
    nwalkers = 100

    # Generate an initial guess for each walker.
    initial = [p0 + 0.01 * np.random.randn(len(p0)) for k in range(nwalkers)]

    # Set up the sampler.
    sampler = emcee.EnsembleSampler(nwalkers, len(p0), line.lnlike,
            args=[data, ])

    # Do a burn in.
    pos, prob, state = sampler.run_mcmc(initial, 100)

    # Clear and start again.
    sampler.reset()
    sampler.run_mcmc(pos, 1000)

    # Take the last 10 steps from each walker.
    chain = sampler.flatchain
    samples = chain[-1000:, :]

    # Compute the mean and standard deviation values for the slope and
    # intercept given these samples.
    m, b = np.mean(samples, axis=0)
    merr, berr = np.std(samples, axis=0)

    # Compute the predicted lines from these samples.
    x = np.array([0, 5])
    lines = samples[:, 0, None] * x[None, :] + samples[:, 1, None]

    # Generate the plot.
    pl.clf()

    # Plot the sampled lines.
    pl.plot(x, lines.T, color="#555555", alpha=0.05)

    # Plot the mean predicted line.
    pl.plot(x, m * x + b, "r", lw=1.5)

    # Over plot the truth.
    pl.plot(x, m_true * x + b_true, "--g", lw=1.5)

    # Over plot the data.
    pl.errorbar(data[:, 0], data[:, 1], yerr=data[:, 2], fmt="ok")

    # Show the results in the title.
    pl.title(r"truth: $(%.1f, %.1f)$, fit: $(%.3f, %.3f) \pm (%.3f, %.3f)$"
            % (m_true, b_true, m, b, merr, berr))

    pl.savefig("samples.png")


if __name__ == "__main__":
    print "Optimizing..."
    optimize()
    print

    print "Sampling..."
    sample()
