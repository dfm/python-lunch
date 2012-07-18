Examples & Source Code for Python Lunch @ MPIA
==============================================

This example code shows how to fit a linear model to noisy data using
[`scipy.optimize`](http://docs.scipy.org/doc/scipy/reference/optimize.html)
and [`emcee`](http://danfm.ca/emcee). The sample data is given in
[this file](https://raw.github.com/dfm/python-lunch/master/data.dat)
and it should look like the following image when plotted:

![](https://github.com/dfm/python-lunch/raw/master/data.png)

where the line is the "truth". Optimizing gives the maximum likelihood
or minimum chi-squared solution to the problem:

![](https://github.com/dfm/python-lunch/raw/master/python/optimize.png)

and sampling using `emcee` gives probabilistic constraints on the
parameters of the linear model:

![](https://github.com/dfm/python-lunch/raw/master/python/samples.png)

Bonus
-----

One of the sweetest features of this tutorial is that it demonstrates
how one might go about doing this same problem with the likelihood
function implemented in
[Python](https://github.com/dfm/python-lunch/tree/master/python),
[C](https://github.com/dfm/python-lunch/tree/master/c)
or [Fortran](https://github.com/dfm/python-lunch/tree/master/fortran)!