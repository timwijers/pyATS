#!/bin/bash

# Author : Tim Wijers
# Copyright (c) Routz B.V
# Script follows here:

apt-get update
apt-get upgrade

apt-get install git
git clone http://github.com/timwijers/pyATS

cd /pyats
source bin/activate
touch testfile.txt
pyats run job jobfile.py




