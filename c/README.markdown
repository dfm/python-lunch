Fitting a Line using *C*
========================

Wrapping C code so that it can be called from Python is a little daunting
and there are [many](http://docs.python.org/c-api/)
[different](http://www.cython.org/) [ways](http://www.swig.org/) to go about
it. Here, we'll directly write the C module and while it looks a little
scary, the structure is actually quite general so a lot of scientific
applications will be possible by mostly copy-and-pasting this example.

References
----------

1. Python docs: [tutorial](http://docs.python.org/extending/)
   and [API](http://docs.python.org/c-api/)
2. [Numpy API reference](http://docs.scipy.org/doc/numpy/reference/c-api.html)
