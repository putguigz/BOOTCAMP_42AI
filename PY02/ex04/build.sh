#!/bin/bash

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade build

mkdir $PWD/dist
python3 -m build ./my-minipack

