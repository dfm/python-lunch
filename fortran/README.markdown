Fitting a Line using *Fortran*
==============================

This module uses [f2py](http://www.scipy.org/F2py/) to wrap a Fortran
likelihood function so that it is callable from Python. `f2py` is part
of `numpy` so anyone with a scientific Python installation should be
able to compile your results. In fact, we'll use `numpy` to do the
compilation.
