import math
import random

class Work():
	def __init__(self, ID, start_node, colony):
		self.ID = ID
		self.start_node = start_node
		self.grouping = colony
		self.curr_node = self.start_node
		self.graph = self.grouping.graph
		self.path_vector = []
		self.path_vector.append(self.start_node)
		self.path_cost = 0
		self.Beta = 1.0
		self.Q0 = 0.5
		self.Rho = 0.99
		self.nodes_to_visit = []
		for i in range(0, self.graph.num_nodes):
			if i != self.start_node:
				self.nodes_to_visit.append(i)
		self.path_matrix = []
		for i in range(0, self.graph.num_nodes):
			self.path_matrix.append([0] * self.graph.num_nodes)

	def run(self):
		graph = self.grouping.graph
		while not len(self.nodes_to_visit) == 0:
			new_node = self.state_transition_rule(self.curr_node)
			self.path_cost += graph.delta_matrix[self.curr_node][new_node]
			self.path_vector.append(new_node)
			self.path_matrix[self.curr_node][new_node] = 1 
			self.local_updating_rule(self.curr_node, new_node)
			self.curr_node = new_node
		self.path_cost += graph.delta_matrix[self.path_vector[-1]][self.path_vector[0]]
		self.grouping.update(self)
		self.__init__(self.ID, self.start_node, self.grouping)

	def state_transition_rule(self, curr_node):
		graph = self.grouping.graph
		q = random.random()
		max_node = -1
		if q < self.Q0:
			#print "Exploitation"
			max_value = -1
			value = None
			for node in self.nodes_to_visit:
				if graph.tau_matrix[curr_node][node] == 0:
					raise Exception("tau = 0")
				value = graph.tau_matrix[curr_node][node] * math.pow(graph.eta(curr_node, node), self.Beta)
				if value > max_value:
					max_value = value
					max_node = node
		else:
			#print "Exploration"
			sum = 0
			node = -1
			for node in self.nodes_to_visit:
				if graph.tau_matrix[curr_node][node] == 0:
					raise Exception("tau = 0")
				sum += graph.tau_matrix[curr_node][node] * math.pow(graph.eta(curr_node, node), self.Beta)
			if sum == 0:
				raise Exception("sum = 0")
			avg = sum / len(self.nodes_to_visit)
			#print "avg = %s" % (avg,)
			for node in self.nodes_to_visit:
				p = graph.tau_matrix[curr_node][node] * math.pow(graph.eta(curr_node, node), self.Beta)
				if p > avg:
					#print "p = %s" % (p,)
					max_node = node
			#if max_node == -1:
				#max_node = node
		if max_node < 0:
			raise Exception("max_node < 0")
		self.nodes_to_visit.remove(max_node)
		return max_node

	def local_updating_rule(self, curr_node, next_node):
		#Update the pheromones on the tau matrix to represent transitions of the ants
		graph = self.grouping.graph
		graph.tau_matrix[curr_node][next_node] = (1 - self.Rho) * graph.tau_matrix[curr_node][next_node] + (self.Rho * graph.tau0)

