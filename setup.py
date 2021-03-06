# from distutils.core import Extension #, setup
from Cython.Build import cythonize
from setuptools import Extension ,setup

# define an extension that will be cythonized and compiled
ext = Extension(name="hello", sources=["hello.pyx"])
setup(ext_modules=cythonize(ext))