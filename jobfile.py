import os

from genie.harness.main import gRun
from pyats.easypy import run

def main():
     test_path = os.path.dirname(os.path.abspath(__file__))
     testscript = os.path.join(test_path, 'set_check_ip_tcs.py')

     run(testscript=testscript)