#!/bin/sh -e
set -x

python3 -m pip install -U pip --quiet
pip install flake8 pytest pytest-cov --quiet

pytest --cache-clear --cov-config=.coveragerc --no-cov-on-fail --cov=src/authk tests/unit/ 
