#!/usr/bin/env python

from distutils.core import setup, Extension
import numpy.distutils.misc_util

c_ext = Extension("line._line", ["line/_line.c", "line/line.c"])

setup(
    name="line",
    author="MPIA Python Lunch",
    packages=["acor"],
    ext_modules=[c_ext],
    include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
)
