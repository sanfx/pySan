#!/usr/bin/env python3
################################
__author__  = "Sanjeev"
__version__ = 1.1
## Branch: pythonic
################################
import sys
import os

def print_environment_variables(variables):
    """Print environment variables (all if variables list is empty)."""
    variables_to_show = variables or sorted(os.environ.keys())
    for index, variable in enumerate(variables_to_show):
        value = os.environ.get(variable) or "[variable does not exist]"
        print("{0}: {1}={2}".format(index, variable, value))

print_environment_variables(sys.argv[1:])