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
		if environment variable name is passed to the enVar function it returns its values.
		"""
		if not isinstance(variable, (tuple, list)):
			raise NoListVariableError('The variable given is not iteratable')

		returnList = []

		for index, var in enumerate(variable):
			try: # converts to upper if user mistakenly enters lowecase
				print "%s %s : %s" % (index, var, os.environ[var])
				returnList.append(var)
			except Exception, e: 
				print 'Make sure the Environment variable "%s" exists or spelled correctly.' % var

		return returnList

	def printEnv(self, variable=None):
		"""This function returns all the environment variable set on the machine or in active project.
		"""
		if not variable:
			print "No Environment variable/s passed. Do you want to print all %s in total(yes or no)?" % len(os.environ)
			choice = raw_input('>>')
			if choice in ['Yes', 'yes', 'y']:
				self.environment_variables(os.environ.keys())
			else:
				#raise EmptyVariableError('No Environment variable given passed.')
				return
		else:
			self.environment_variables(variable)


def izip(*iterables):
	""" izip available in Python 3 backporting for python 2.6
	# izip('ABCD', 'xy') --> Ax By
	"""
    	iterators = map(iter, iterables)
    	while iterators:
    		yield tuple(map(next, iterators))


# import sys

# showEnVar = Show()
# showEnVar.printEnv(sys.argv[1:])
