#!/usr/bin/env mpcpython
################################
__author__  = "Sanjeev"
__version__ = 1.2
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
		pass

	def environment_variables(self,variable=None):
		"""
		This function returns all the environment variable set on the machine or in active project.
		if environment variable name is passed to the enVar function it returns its values.
		"""


		if not isinstance(variable, (tuple, list)):
			raise NoListVariableError('The variable given is not itaratable')

		nVar = len(variable)
		returnList = []

		# if not any(variable): # if user entered no environment variable name
		# 	for index, each in enumerate(sorted(os.environ.iteritems())):
		# 		print "%s %s: %s" %(index, each[0], each[1])
		# else: # if user entered one or more than one environment variable name
		for var in variable:
			if os.environ.get(var.upper()): # convertes to upper if user mistakenly enters lowecase
				print "%s : %s" % (var.upper(), os.environ.get(var.upper()))
				returnList.append(var)
			else: 
				print 'Make sure the Environment variable "%s" exists or spelled correctly.' % var
		return returnList

	def printEnv(self, variable=None):
		if not variable:
			print "No Environment variable/s passed. Do you want to print all %s in total(yes or no)?" % len(os.environ)
			choice = raw_input('>>')
			if choice in ['Yes', 'yes', 'y']:
				self.environment_variables(os.environ.keys())
			else:
				raise EmptyVariableError('No Environment variable given passed.')
				#return
		else:
			self.environment_variables(variable)