import unittest
import pickle

class TestFunctions(unittest.TestCase):
	def test2(self):
		results = pickle.load(open("outputs/output2.pickled", "r"))
		self.assertTrue(results[2]==4366)

	def test3(self):
		results = pickle.load(open("outputs/output3.pickled", "r"))
		self.assertTrue(results[2]==4908)

	def test4(self):
		results = pickle.load(open("outputs/output4.pickled", "r"))
		self.assertTrue(results[2]==5313)

	def test5(self):
		results = pickle.load(open("outputs/output5.pickled", "r"))
		self.assertTrue(results[2]==5396)

	def test6(self):
		results = pickle.load(open("outputs/output6.pickled", "r"))
		self.assertTrue(results[2]==5464)

	def test7(self):
		results = pickle.load(open("outputs/output7.pickled", "r"))
		self.assertTrue(results[2]==5463)

	def test8(self):
		results = pickle.load(open("outputs/output8.pickled", "r"))
		self.assertTrue(results[2]==5453)

	def test9(self):
		results = pickle.load(open("outputs/output9.pickled", "r"))
		self.assertTrue(results[2]==5455)

	def test10(self):
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525)

	def test11(self):
		results = pickle.load(open("outputs/output11.pickled", "r"))
		self.assertTrue(results[2]==5678)

	def test12(self):
		results = pickle.load(open("outputs/output12.pickled", "r"))
		self.assertTrue(results[2]==5782)

	def test13(self):
		results = pickle.load(open("outputs/output13.pickled", "r"))
		self.assertTrue(results[2]==5868)

	def test14(self):
		results = pickle.load(open("outputs/output14.pickled", "r"))
		self.assertTrue(results[2]==6065)

if __name__ == '__main__':
    unittest.main()
