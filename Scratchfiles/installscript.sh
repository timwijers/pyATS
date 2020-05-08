#!/bin/bash

# Author : Tim Wijers
# Copyright (c) Routz B.V
# Script follows here:

#apt-get update
#apt-get upgrade

cd /pyats/pyATS
git pull http://github.com/timwijers/pyATS

pyats run job jobfile.py




