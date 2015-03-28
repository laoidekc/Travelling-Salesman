import math
import random

class Work():
	def __init__(self, ID, start_node, colony):
		self.ID = ID
		self.start_node = start_node
		self.grouping = colony
		self.current_node = self.start_node
		self.graph = self.grouping.graph
		self.path_vector = []
		self.path_vector.append(self.start_node)
		self.path_cost = 0
		self.Beta = 1.0
		self.exploitation_chance = 0.5
		self.Rho = 0.99
		self.nodes_to_visit = []
		for i in range(0, self.graph.num_nodes):
			if i != self.start_node:
				self.nodes_to_visit.append(i)
		self.path_matrix = []
		for i in range(0, self.graph.num_nodes):
			self.path_matrix.append([0] * self.graph.num_nodes)

	#creates new path
	def run(self):
		graph = self.grouping.graph
		while not len(self.nodes_to_visit) == 0:
			new_node = self.state_transition_rule(self.current_node)
			self.path_cost += graph.delta_matrix[self.current_node][new_node]
			self.path_vector.append(new_node)
			self.path_matrix[self.current_node][new_node] = 1 
			self.local_updating_rule(self.current_node, new_node)
			self.current_node = new_node
		self.path_cost += graph.delta_matrix[self.path_vector[-1]][self.path_vector[0]]
		self.grouping.update(self)
		self.__init__(self.ID, self.start_node, self.grouping)

	#chooses next node to visit
	def state_transition_rule(self, current_node):
		graph = self.grouping.graph
		max_node = -1
		#chooses node with maximum value
		if random.random() < self.exploitation_chance:
			if __debug__:
				print "Exploitation"
			max_value = -1
			for node in self.nodes_to_visit:
				if graph.tau_matrix[current_node][node] == 0:
					raise Exception("tau = 0")
				value = graph.tau_matrix[current_node][node] * math.pow(graph.eta(current_node, node), self.Beta)
				if value > max_value:
					max_value = value
					max_node = node

		#chooses node with  above average value
		else:
			if __debug__:
				print "Exploration"
			sum = 0
			for node in self.nodes_to_visit:
				if graph.tau_matrix[current_node][node] == 0:
					raise Exception("tau = 0")
				sum += graph.tau_matrix[current_node][node] * math.pow(graph.eta(current_node, node), self.Beta)
			if sum == 0:
				raise Exception("sum = 0")
			average = sum / len(self.nodes_to_visit)
			if __debug__:
				print "average = %s" % (average,)
			for node in self.nodes_to_visit:
				if graph.tau_matrix[current_node][node] * math.pow(graph.eta(current_node, node), self.Beta) >= average:
					max_node = node
					if __debug__:
						print  "p = %s" % (graph.tau_matrix[current_node][node] * math.pow(graph.eta(current_node, node), self.Beta),)
		if max_node < 0:
			raise Exception("max_node < 0")
		self.nodes_to_visit.remove(max_node)
		return max_node

	def local_updating_rule(self, current_node, next_node):
		#Update the tau matrix to represent transitions of the ants
		graph = self.grouping.graph
		graph.tau_matrix[current_node][next_node] = (1 - self.Rho) * graph.tau_matrix[current_node][next_node] + (self.Rho * graph.tau0)

