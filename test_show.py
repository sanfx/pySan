import unittest
import show

class TestShowEnVariables(unittest.TestCase):

	def setUp(self):
		self.shoEnVar = show.Show()
		# shoEnVar.environment_variables()


	def test_environment_variables(self):
		self.assertEqual(self.shoEnVar.environment_variables(['USER']), ['USER'])
		self.assertEqual(self.shoEnVar.environment_variables(['USER', 'LADSKFJ']), ['USER'])
		self.assertNotEqual(self.shoEnVar.environment_variables(['USER', 'LADSKFJ']), ['USER', 'LADSKFJ'])

		self.assertRaises(show.NoListVariableError, self.shoEnVar.environment_variables, 'USER')
		# self.assertRaises(show.NoVariableError, self.shoEnVar.environment_variables, ['vc6v5'])
		self.assertRaises(show.EmptyVariableError, self.shoEnVar.environment_variables, None)
if __name__ == '__main__':
	unittest.main()

self.shoEnVar.environment_variables(['USER', 'LADSKFJ'])