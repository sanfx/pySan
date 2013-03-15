import unittest
import Tank

class TestTank(unittest.TestCase):

	def setUp(self):
		self.tank = Tank.Tank()


	def testTankhasImage(self):
		
		assert self.tank.image != None, "tank image is None"

	def testTankhasRect(self):

		assert self.tank.rect != None, "tank rectangale is None"

if __name__ == '__main__':
	unittest.main()