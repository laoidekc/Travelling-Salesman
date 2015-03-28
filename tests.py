import unittest
import pickle
import random
import travelling_salesman

class TestFunctions(unittest.TestCase):
	def setUp(self):
		random.seed(227)

	def test2(self):
		argv = [2, "citiesAndDistances.pickled", "outputs/output2.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output2.pickled", "r"))
		self.assertTrue(results[2]==4366)


	def test3(self):
		argv = [3, "citiesAndDistances.pickled", "outputs/output3.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output3.pickled", "r"))
		self.assertTrue(results[2]==4908)

	def test4(self):
		argv = [4, "citiesAndDistances.pickled", "outputs/output4.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output4.pickled", "r"))
		self.assertTrue(results[2]==5313)

	def test5(self):
		argv = [5, "citiesAndDistances.pickled", "outputs/output5.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output5.pickled", "r"))
		self.assertTrue(results[2]==5396)

	def test6(self):
		argv = [6, "citiesAndDistances.pickled", "outputs/output6.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output6.pickled", "r"))
		self.assertTrue(results[2]==5464)

	def test7(self):
		argv = [7, "citiesAndDistances.pickled", "outputs/output7.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output7.pickled", "r"))
		self.assertTrue(results[2]==5463)


	def test8(self):
		argv = [8, "citiesAndDistances.pickled", "outputs/output8.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output8.pickled", "r"))
		self.assertTrue(results[2]==5453)

	def test9(self):
		argv = [9, "citiesAndDistances.pickled", "outputs/output9.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525)

	def test10(self):
		argv = [10, "citiesAndDistances.pickled", "outputs/output10.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525)

	def test11(self):
		argv = [11, "citiesAndDistances.pickled", "outputs/output11.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output11.pickled", "r"))
		self.assertTrue(results[2]==5678)

	def test12(self):
		argv = [12, "citiesAndDistances.pickled", "outputs/output12.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output12.pickled", "r"))
		self.assertTrue(results[2]==5782)

	def test13(self):
		argv = [13, "citiesAndDistances.pickled", "outputs/output13.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output13.pickled", "r"))
		self.assertTrue(results[2]==5868)

	def test14(self):
		argv = [14, "citiesAndDistances.pickled", "outputs/output14.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output14.pickled", "r"))
		self.assertTrue(results[2]==6065)

if __name__ == '__main__':
    unittest.main()
