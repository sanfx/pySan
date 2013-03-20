#!/usr/bin/env mpcpython
import unittest
from mpc.testing.testBase import TestCase
import show

class TestShowEnVariables(TestCase):

	def setUp(self):
		super(TestShowEnVariables,self).setUp()
		self.shoEnVar = show.Show()


	def test_environment_variables(self):
		self.assertEqual(self.shoEnVar.environment_variables(['USER']), ['USER'])
		self.assertEqual(self.shoEnVar.environment_variables(['USER', 'LADSKFJ']), ['USER'])
		self.assertNotEqual(self.shoEnVar.environment_variables(['USER', 'LADSKFJ']), ['USER', 'LADSKFJ'])

		self.assertRaises(show.NoListVariableError, self.shoEnVar.environment_variables, 'USER')
		# self.assertRaises(show.NoVariableError, self.shoEnVar.environment_variables, ['vc6v5'])
		self.assertRaises(show.EmptyVariableError, self.shoEnVar.environment_variables, None)

	def test_printEnv(self):
		self.assertEqual(self.shoEnVar.printEnv(['USER']),['USER'])
		#self.assertEqual(self.shoEnVar.printEnv(['USER', 'LADSKFJ']), ['USER'])
		#self.assertNotEqual(self.shoEnVar.printEnv(['USER', 'LADSKFJ']), ['USER', 'LADSKFJ'])

		#self.assertRaises(show.NoListVariableError, self.shoEnVar.printEnv, 'USER')
		# self.assertRaises(show.NoVariableError, self.shoEnVar.printEnv, ['vc6v5'])
		#self.assertRaises(show.EmptyVariableError, self.shoEnVar.printEnv, None)

if __name__ == '__main__':
	unittest.main()
