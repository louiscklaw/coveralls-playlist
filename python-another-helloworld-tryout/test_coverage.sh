#!/usr/bin/env bash

set -ex


# pip install coveralls
# pipenv install coverage==5.0.1
# pipenv install pytest-cov
# pipenv install coveralls==1.10.0

pipenv sync --dev

pytest tests/test.py
