#!/usr/bin/env python
################################
## Sanjeev
## Version: 1.0
################################
import os, sys
variable  = ""
try:
        nVar = len(sys.argv)-1
	variable =  sys.argv[1]
except:
	variable = None

def enVar(variable=None):
        """
        This function returns all the environment variable set on the machine or in active project.
        if environment variable name is passed to the enVar function it returns its values.
        """
        if variable==None:
                for index, each in enumerate(os.environ.iteritems()):
                        print index, each
        else:

        	if os.environ.get(variable):
        		print "%s : %s" %  (variable, os.environ.get(variable))
        	else: print 'Make sure the Environment variable "%s" exists or spelled correctly.' % variable

enVar(variable)
