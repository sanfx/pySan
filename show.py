#!/usr/bin/env python3
################################
__author__  = "Sanjeev"
__version__ = 1.1
################################
import sys
import os

def print_environment_variables(variables):
    """Print environment variables (all if variables list is empty)."""
    if not variables:
        for index, (variable, value) in enumerate(sorted(os.environ.items())):
            print("{0}: {1}".format(variable, value))
    else: 
        for variable in variables:
          value = os.environ.get(variable)
          if value:
              print("{0}: {1}".format(variable, value))
          else:
            print("Variable does not exist: {0}".format(variable))

print_environment_variables(sys.argv[1:])