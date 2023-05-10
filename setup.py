#!/usr/bin/env python



import setuptools
from distutils.errors import DistutilsError
from numpy.distutils.core import setup, Extension, build_ext, build_src
from distutils.sysconfig import get_config_var, get_config_vars
import versioneer
import os, sys
import subprocess as sp
import numpy as np
build_ext = build_ext.build_ext
build_src = build_src.build_src

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements       = []
setup_requirements = []
test_requirements  = []

compile_opts = {
    'extra_compile_args': ['-std=c99','-fopenmp', '-Wno-strict-aliasing', '-g'],
    'extra_f90_compile_args': ['-fopenmp', '-Wno-conversion', '-Wno-tabs'],
    'extra_link_args': ['-fopenmp', '-g']
    }

fcflags = os.getenv('FCFLAGS')
if fcflags is None or fcflags.strip() == '':
    fcflags = ['-O3']
else:
    print('User supplied fortran flags: ', fcflags)
    print('These will supersede other optimization flags.')
    fcflags = fcflags.split()
    
compile_opts['extra_f90_compile_args'].extend(fcflags)

    


class CustomBuild(build_ext):
    def run(self):
        # Then let setuptools do its thing.
        return build_ext.run(self)

class CustomSrc(build_src):
    def run(self):
        # Then let setuptools do its thing.
        return build_src.run(self)

class CustomEggInfo(setuptools.command.egg_info.egg_info):
    def run(self):
        return setuptools.command.egg_info.egg_info.run(self)   

# Cascade your overrides here.
cmdclass = {
    'build_ext': CustomBuild,
    'build_src': CustomSrc,
    'egg_info': CustomEggInfo,
}
cmdclass = versioneer.get_cmdclass(cmdclass)


if __name__ == "__main__":
    setup(name='lensingbiases',
        version='1.0.0',
        author='Antony Lewis, Julien Peloton',
        author_email='j.peloton@sussex.ac.uk',
        packages=['lensingbiases'],
        ext_modules=[
            Extension('lensingbiases._lensing_biases',
                sources=['LensingBiases.f90'],
                **compile_opts),
        ],
        zip_safe=False,
        cmdclass=cmdclass,
        description='Compute lensing biases N0 and N1',)
