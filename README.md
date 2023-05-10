# About this fork

This is a very sketchy edit to setup.py to get lensingbiases to compile for Python 3. I haven't changed anything else so most of the python code might not work, but this way we can call the FORTRAN code from python 3. 


To compile
```bash
python setup.py build_ext -i
pip install -e . --user
```


And to call the N0 and N1 bias calculation code
```python
from lensingbiases._lensing_biases import lensingbiases as bias
```
Where now we have access to `bias.compute_n0` and `bias.compute_n1` part of the FORTRAN code.


Below is the old README


Lensingbiases
==

Computation of N0 and N1 biases in the context of CMB weak lensing (flat-sky approximation).
Derivatives of N1 biases with respect to the lensing potential power-spectrum available.

License: GNU License (see the LICENSE file for details) covers all files
in the lensingbiases repository unless stated otherwise.

### Before starting
The Python code has the following dependencies:
* numpy, pylab, argparse
* f2py

In most machines, those packages are automatically installed.
Make sure you update your PYTHONPATH to use the code.
Just add in your bashrc:
```bash
BIASPATH=/path/to/the/package
export PYTHONPATH=$PYTHONPATH:$BIASPATH
```

### Compilation of Fortran
The package is written in python, but internal operations are
done in Fortran. Therefore you need to compile it before using
the routines. We provide a setup file. Just run:
```bash
python setup.py build_ext --inplace --fcompiler=gfortran
```
Depending on system, you may need to specify a different fortran compiler.
For the purist, we also provide a Makefile for a direct compilation.
For extended multipole ranges, computation can be long.
So make sure that you are using several processors by adding in your bashrc:
```bash
export OMP_NUM_THREADS=n
```

### Usage
User has to provide the range of multipole, beam width, noise level, etc.
In order to ease the start, we provide both a test script and a launcher:
* LensingBiases.py (see the main)
* launch.sh

For usage on clusters, we also provide a batch (SLURM).
