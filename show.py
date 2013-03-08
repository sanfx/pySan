#!/usr/bin/env mpcpython
################################
## Sanjeev
## Version: 1.1
################################
import os, sys

variable =  sys.argv

def enVar(variable):
        """
        This function returns all the environment variable set on the machine or in active project.
        if environment variable name is passed to the enVar function it returns its values.
        """
        nVar = len(sys.argv)-1
        if len(variable)== 1: # if user entered no environment variable name
                for index, each in enumerate(os.environ.iteritems()):
                        print index, each
        else: # if user entered one or more than one environment variable name
                for x in range(nVar):
                        x+=1
                        if os.environ.get(variable[x]):
                                print "%s : %s" %  (variable[x], os.environ.get(variable[x]))
        	        else: print 'Make sure the Environment variable "%s" exists or spelled correctly.' % variable[x]

enVar(variable)