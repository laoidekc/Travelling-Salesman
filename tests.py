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
		self.assertTrue(results[2]==4366,"Incorrect path for 2 cities. This may be because the file citiesAndDistances.pickled has been changed")


	def test3cities(self):
		argv = [3, "citiesAndDistances.pickled", "outputs/output3.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output3.pickled", "r"))
		self.assertTrue(results[2]==4908,"Incorrect path for 3 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test4cities(self):
		argv = [4, "citiesAndDistances.pickled", "outputs/output4.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output4.pickled", "r"))
		self.assertTrue(results[2]==5313,"Incorrect path for 4 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test5cities(self):
		argv = [5, "citiesAndDistances.pickled", "outputs/output5.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output5.pickled", "r"))
		self.assertTrue(results[2]==5396,"Incorrect path for 5 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test6cities(self):
		argv = [6, "citiesAndDistances.pickled", "outputs/output6.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output6.pickled", "r"))
		self.assertTrue(results[2]==5464,"Incorrect path for 6 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test7cities(self):
		argv = [7, "citiesAndDistances.pickled", "outputs/output7.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output7.pickled", "r"))
		self.assertTrue(results[2]==5463,"Incorrect path for 7 cities. This may be because the file citiesAndDistances.pickled has been changed")


	def test8cities(self):
		argv = [8, "citiesAndDistances.pickled", "outputs/output8.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output8.pickled", "r"))
		self.assertTrue(results[2]==5453,"Incorrect path for 8 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test9cities(self):
		argv = [9, "citiesAndDistances.pickled", "outputs/output9.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525,"Incorrect path for 9 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test10cities(self):
		argv = [10, "citiesAndDistances.pickled", "outputs/output10.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output10.pickled", "r"))
		self.assertTrue(results[2]==5525,"Incorrect path for 10 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test11cities(self):
		argv = [11, "citiesAndDistances.pickled", "outputs/output11.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output11.pickled", "r"))
		self.assertTrue(results[2]==5678,"Incorrect path for 11 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test12cities(self):
		argv = [12, "citiesAndDistances.pickled", "outputs/output12.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output12.pickled", "r"))
		self.assertTrue(results[2]==5782,"Incorrect path for 12 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test13cities(self):
		argv = [13, "citiesAndDistances.pickled", "outputs/output13.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output13.pickled", "r"))
		self.assertTrue(results[2]==5868,"Incorrect path for 13 cities. This may be because the file citiesAndDistances.pickled has been changed")

	def test14cities(self):
		argv = [14, "citiesAndDistances.pickled", "outputs/output14.pickled"]
		travelling_salesman.main(argv)
		results = pickle.load(open("outputs/output14.pickled", "r"))
		self.assertTrue(results[2]==6065,"Incorrect path for 14 cities. This may be because the file citiesAndDistances.pickled has been changed")

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
		random.seed(227)
		num_nodes = 3
		distances = [[i+num_nodes*j for i in range(num_nodes)] for j in range(num_nodes)]
		self.graph = graphbit.GraphBit(num_nodes,distances)
		self.group = biggroup.BigGroup(self.graph,1,1)

	def test_initialisation(self):
		self.assertTrue(self.group.best_path_cost==sys.maxint,"Best path cost intialised incorrectly")
		self.assertTrue(self.group.best_path_vector==None,"Best path vector intialised incorrectly")
		self.assertTrue(self.group.best_path_matrix==None,"Best path matrix intialised incorrectly")

	def test_start(self):
		self.graph.reset_tau()
		self.group.start()
		self.assertTrue(self.group.best_path_cost==12,"Producing incorrect best path cost")

	def test_iteration(self):
		self.graph.reset_tau()
		self.group.iter_counter = 0
		self.group.ants = self.group.colony_workers()
		self.group.iteration()
		self.assertTrue(self.group.best_path_cost==12,"Iteration prducing incorrect best path cost")
		self.assertTrue(self.group.best_path_vector==[1,0,2],"Iteration producing incorrect best path vector")
		self.assertTrue(self.group.best_path_matrix==[[0, 0, 1], [1, 0, 0], [0, 0, 0]],"Iteration producing incorrect best path matrix")

	def test_update(self):
		ant = work.Work(0, random.randint(0, self.graph.num_nodes - 1), self)
		self.group.ant_counter = 0
		self.group.average_path_cost = 0
		self.group.iter_counter = 0
		self.group.ants = []
		self.group.ants.append(ant)
		ant.path_cost = 77
		ant.path_vector = [0,1,2]
		ant.path_matrix = [[0,0,1],[0,1,0],[0,0,0]]
		self.group.update(ant)
		self.assertTrue(self.group.best_path_cost==77,"Updating changes best path cost")
		self.assertTrue(self.group.best_path_vector==[0,1,2],"Updating changes best path vector")
		self.assertTrue(self.group.best_path_matrix==[[0,0,1], [0,1,0], [0,0,0]],"Updating changes best path matrix")

	def test_colony(self):
		ants = self.group.colony_workers()
		self.assertTrue(ants[0].nodes_to_visit==[0,2],"Starting colony assigns incorrect unvisited nodes")
		self.assertTrue(ants[0].path_vector==[1],"Starting colony assigns incorrect starting node")

	def test_global(self):
		self.graph.reset_tau()
		self.group.Alpha = 0.1
		self.group.ants = self.group.colony_workers()
		self.group.iter_counter = 0
		self.group.iteration()
		self.group.global_updating_rule()
		self.assertTrue(self.graph.tau_matrix==[[0.16666666666666666, 0.15, 0.15833333333333333], [0.15833333333333333, 0.16666666666666666, 0.15], [0.15, 0.15, 0.16666666666666666]],"Global updating results in incorrect tau matrix")

class work_tests(unittest.TestCase):
	def setUp(self):
		random.seed(227)
		num_nodes = 3
		distances = [[i+num_nodes*j for i in range(num_nodes)] for j in range(num_nodes)]
		self.graph = graphbit.GraphBit(num_nodes,distances)
		self.group = biggroup.BigGroup(self.graph,1,1)
		self.group.ants = []
		self.ant = work.Work(1, random.randint(0, self.graph.num_nodes - 1), self.group)
		self.group.ants.append(self.ant)

	def test_initialisation(self):
		self.assertTrue(self.ant.nodes_to_visit==[0,2],"Work initialises incorrect unvisited nodes")
		self.assertTrue(self.ant.path_vector==[1],"Work initialises incorrect starting node")
		
	def test_run(self):
		self.graph.reset_tau()
		self.group.ant_counter = 0
		self.group.average_path_cost = 0
		self.group.iter_counter = 0
		self.ant.run()
		self.assertTrue(self.group.best_path_cost==12,"Run function produces incorrect best path cost")
		self.assertTrue(self.group.best_path_vector==[1,0,2],"Run function produces incorrect best path vector")
		self.assertTrue(self.group.best_path_matrix==[[0, 0, 1], [1, 0, 0], [0, 0, 0]],"Run function produces incorrect best path matrix")

	def test_state_transition(self):
		self.graph.reset_tau()
		nodes = []
		nodes.append(self.ant.current_node)
		for i in range (0,2):
			self.ant.current_node = self.ant.state_transition_rule(self.ant.current_node)
			nodes.append(self.ant.current_node)
		self.assertTrue(nodes==[1,0,2],"State transition rule visits nodes in incorrect order")

	def test_local_updating(self):
		self.graph.reset_tau()
		self.ant.Rho = 0.99
		self.ant.local_updating_rule(0,1)
		self.assertAlmostEqual(self.graph.tau_matrix[0][1],0.166666666667,7,"Local updating rule gives incorrect value")

if __name__ == '__main__':
	#Add the names of test classes to this list in order to have them run.
	#Remove the names of any uneccesary test classes.
	test_classes_to_run = [main_tests, graphbit_tests, biggroup_tests, work_tests]

	loader = unittest.TestLoader()

	suites_list = []
	for test_class in test_classes_to_run:
		suite = loader.loadTestsFromTestCase(test_class)
		suites_list.append(suite)

	big_suite = unittest.TestSuite(suites_list)

	runner = unittest.TextTestRunner()
	results = runner.run(big_suite)
