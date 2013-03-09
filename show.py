#!/usr/bin/env python26
################################
__author__  = "Sanjeev"
__version__ = 1.1
################################
import os
import sys

print sys.argv[1:]

def environment_variables(variable):
        """
        This function returns all the environment variable set on the machine or in active project.
        if environment variable name is passed to the enVar function it returns its values.
        """
        nVar = len(sys.argv)-1
        print any(variable)
        if not any(variable): # if user entered no environment variable name
                for index, each in enumerate(sorted(os.environ.iteritems())):
                        print "%s %s: %s" %(index, each[0], each[1])
        else: # if user entered one or more than one environment variable name
                for x in range(nVar):
                        if os.environ.get(variable[x].upper()): # convertes to upper if user mistakenly enters lowecase
                                print "%s : %s" %  (variable[x].upper(), os.environ.get(variable[x].upper()))
        	        else: print 'Make sure the Environment variable "%s" exists or spelled correctly.' % variable[x]

environment_variables(sys.argv[1:])