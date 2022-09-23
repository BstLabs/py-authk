#!/bin/sh -e
set -x

python3 -m pip install -U pip --quiet
pip install flake8 pytest pytest-cov --quiet

pytest --cache-clear --no-cov-on-fail --cov=src/authk test/unit/ 
