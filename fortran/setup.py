#!/usr/bin/env python

import subprocess

from numpy.distutils.core import setup, Extension


# Generate the Fortran signature/interface.
cmd = "cd line;f2py line.f -m _line -h line.pyf --overwrite-signature"
subprocess.call(cmd, shell=True)

# Define the Fortran extension.
f_ext = Extension("line._line", ["line/line.pyf", "line/line.f"])

setup(
    name="line",
    author="MPIA Python Lunch",
    packages=["line"],
    ext_modules=[f_ext],
)
