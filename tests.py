import unittest
import pickle
import random
import travelling_salesman
import graphbit
import biggroup
import work
import sys

class main_tests(unittest.TestCase):

	def setUp(self):
		random.seed(227)

	def test2cities(self):
		argv = [2, "citiesAndDistances.pickled", "outputs/output2.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output2.pickled", "r"))
		self.assertTrue(results[2]==4366,"Incorrect path for 2 cities")


	def test3cities(self):
		argv = [3, "citiesAndDistances.pickled", "outputs/output3.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output3.pickled", "r"))
		self.assertTrue(results[2]==4908,"Incorrect path for 3 cities")

	def test4cities(self):
		argv = [4, "citiesAndDistances.pickled", "outputs/output4.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output4.pickled", "r"))
		self.assertTrue(results[2]==5313,"Incorrect path for 4 cities")

	def test5cities(self):
		argv = [5, "citiesAndDistances.pickled", "outputs/output5.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output5.pickled", "r"))
		self.assertTrue(results[2]==5396,"Incorrect path for 5 cities")

	def test6cities(self):
		argv = [6, "citiesAndDistances.pickled", "outputs/output6.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output6.pickled", "r"))
		self.assertTrue(results[2]==5464,"Incorrect path for 6 cities")

	def test7cities(self):
		argv = [7, "citiesAndDistances.pickled", "outputs/output7.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output7.pickled", "r"))
		self.assertTrue(results[2]==5463,"Incorrect path for 7 cities")


	def test8cities(self):
		argv = [8, "citiesAndDistances.pickled", "outputs/output8.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output8.pickled", "r"))
		self.assertTrue(results[2]==5453,"Incorrect path for 8 cities")

	def test9cities(self):
		argv = [9, "citiesAndDistances.pickled", "outputs/output9.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525,"Incorrect path for 9 cities")

	def test10cities(self):
		argv = [10, "citiesAndDistances.pickled", "outputs/output10.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525,"Incorrect path for 10 cities")

	def test11cities(self):
		argv = [11, "citiesAndDistances.pickled", "outputs/output11.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output11.pickled", "r"))
		self.assertTrue(results[2]==5678,"Incorrect path for 11 cities")

	def test12cities(self):
		argv = [12, "citiesAndDistances.pickled", "outputs/output12.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output12.pickled", "r"))
		self.assertTrue(results[2]==5782,"Incorrect path for 12 cities")

	def test13cities(self):
		argv = [13, "citiesAndDistances.pickled", "outputs/output13.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output13.pickled", "r"))
		self.assertTrue(results[2]==5868,"Incorrect path for 13 cities")

	def test14cities(self):
		argv = [14, "citiesAndDistances.pickled", "outputs/output14.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output14.pickled", "r"))
		self.assertTrue(results[2]==6065,"Incorrect path for 14 cities")

class graphbit_tests(unittest.TestCase):

	def setUp(self):
		self.num_nodes = 3
		self.distances = [[i+self.num_nodes*j for i in range(self.num_nodes)] for j in range(self.num_nodes)]
		self.graph = graphbit.GraphBit(self.num_nodes,self.distances)

	def test_initialisation(self):
		self.assertTrue(len(self.graph.tau_matrix)==self.num_nodes,"Initialising graph does not give correctly sized tau matrix")
	
	def test_eta(self):
		self.assertTrue(self.graph.eta(2,2)==0.125,"Eta function is not returning inverse of matrix element")

	def test_reset(self):
		self.graph.reset_tau()
		for r in range(0, self.num_nodes):
			for s in range(0, self.num_nodes):
				if self.graph.tau_matrix[r][s] - 0.166667 > 0.000001:
					self.fail("Tau reset to incorrect value")

	def test_average(self):
		self.assertTrue(self.graph.average(self.distances)==4,"Average function is not correctly returning the average of the matrix elements")

class biggroup_tests(unittest.TestCase):

	def setUp(self):
		num_nodes = 3
		distances = [[i+num_nodes*j for i in range(num_nodes)] for j in range(num_nodes)]
		self.graph = graphbit.GraphBit(num_nodes,distances)
		self.group = biggroup.BigGroup(self.graph,1,1)

	def test_initialisation(self):
		self.assertTrue(self.group.best_path_cost==sys.maxint,"Best path cost intialised incorrectly")
		self.assertTrue(self.group.best_path_vector==None,"Best path vector intialised incorrectly")
		self.assertTrue(self.group.best_path_matrix==None,"Best path matrix intialised incorrectly")

	def test_start(self):
		random.seed(227)
		self.graph.reset_tau()
		self.group.start()
		self.assertTrue(self.group.best_path_cost==12,"Producing incorrect best path cost")
		
if __name__ == '__main__':
	unittest.main()
