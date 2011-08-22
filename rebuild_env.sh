#!/usr/bin/env bash

export PIP_USE_MIRRORS=true
venv=.venv
ROOT=`dirname $0`

echo "Cleaning virtualenv..."
rm -rf ${venv}

echo "Creating venv..."
virtualenv -q --no-site-packages ${venv} -p python2.6
echo "done."
source ${venv}/bin/activate
#PIP_REQUIRES=${ROOT}/pip-requires
pip install -E ${venv} lettuce # -r ${PIP_REQUIRES} --upgrade --mirrors http://ppc-pypi1.ppc.griddynamics.net
#gnuplot --version > /dev/null 2> /dev/null || echo 'WARNING: It seems that GNU Plot is not installed. You should install it to generate performance charts.'
