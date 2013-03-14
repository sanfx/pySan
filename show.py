#!/usr/bin/env mpcpython
################################
__author__  = "Sanjeev"
__version__ = 1.1
################################
import os
import sys

class EmptyVariableError(Exception):
        pass


class NoVariableError(Exception):
        pass


class NoListVariableError(Exception):
        pass


class Show(object):
        def __init__(self):
                #self.environment_variables(sys.argv[1:])
                pass


        def environment_variables(self,variable=None):
                """
                This function returns all the environment variable set on the machine or in active project.
                if environment variable name is passed to the enVar function it returns its values.
                """
                if not variable:
                        raise EmptyVariableError('The variable given is empty')

                if not isinstance(variable, (tuple, list)):
                        raise NoListVariableError('The variable given is not itaratable')

                nVar = len(variable)
                returnList = []

                if not any(variable): # if user entered no environment variable name
                        for index, each in enumerate(sorted(os.environ.iteritems())):
                                print "%s %s: %s" %(index, each[0], each[1])
                else: # if user entered one or more than one environment variable name
                        for x in range(nVar):
                                if os.environ.get(variable[x].upper()): # convertes to upper if user mistakenly enters lowecase
                                        print "%s : %s" % (variable[x].upper(), os.environ.get(variable[x].upper()))
                                        returnList.append(variable[x])
                                else: 
                                        print 'Make sure the Environment variable "%s" exists or spelled correctly.' % variable[x]
                return returnList