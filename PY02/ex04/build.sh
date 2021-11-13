#!/bin/bash

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade build

python3 -m build ./my_minipack
pip install ./my_minipack/dist/my_minipack-1.0.0.tar.gz

