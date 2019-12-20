from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy
setup(ext_modules = cythonize("*.pyx", annotate=True),
    include_dirs=[numpy.get_include()])

# python3 setup.py build_ext --inplace
