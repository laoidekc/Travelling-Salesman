import work
import sys
import random

class BigGroup:
	#initialises ant colony
	def __init__(self, graph, num_ants, num_iterations):
		self.graph = graph
		self.num_ants = num_ants
		self.num_iterations = num_iterations
		self.Alpha = 0.1
		self.reset()

	#ensures that there is no preset best path
	def reset(self):
		self.best_path_cost = sys.maxint
		self.best_path_vector = None
		self.best_path_matrix = None

	#starts the testing
	def start(self):
		self.ants = self.colony_workers()
		self.iter_counter = 0

		while self.iter_counter < self.num_iterations:
			self.iteration()
			# Note that this will help refine the results future iterations.
			self.global_updating_rule()

	#begins new iteration of ants
	def iteration(self):
		self.average_path_cost = 0
		self.ant_counter = 0
		self.iter_counter += 1
		for ant in self.ants:
			ant.run()

	#updates best path and average path values when an ant is finished
	def update(self, ant):
		if __debug__:
			print "Update called by %s" % (ant.ID,)
		self.ant_counter += 1
		self.average_path_cost += ant.path_cost
		if ant.path_cost < self.best_path_cost:
			self.best_path_cost = ant.path_cost
			self.best_path_matrix = ant.path_matrix
			self.best_path_vector = ant.path_vector
		if self.ant_counter == len(self.ants):
			self.average_path_cost /= len(self.ants)
			print "Iteration %s: %s - %s" % (self.iter_counter, self.best_path_vector, self.best_path_cost,)

	#assigns each ant some work to do
	def colony_workers(self):
		self.reset()
		ants = []
		for i in range(0, self.num_ants):
			ant = work.Work(i, random.randint(0, self.graph.num_nodes - 1), self)
			ants.append(ant)

		return ants

	#updates tau matrix to improve future iterations
	def global_updating_rule(self):
		evaporation = 0
		deposition = 0
		for r in range(0, self.graph.num_nodes):
			for s in range(0, self.graph.num_nodes):
				if r != s:
					delta_tau = self.best_path_matrix[r][s] / self.best_path_cost
					evaporation = (1 - self.Alpha) * self.graph.tau_matrix[r][s]
					deposition = self.Alpha * delta_tau
					self.graph.tau_matrix[r][s] =  evaporation + deposition

