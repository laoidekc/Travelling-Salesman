class GraphBit:
	def __init__(self, num_nodes, delta_matrix, tau_matrix=None):
#		print len(delta_matrix)
		if len(delta_matrix) != num_nodes:
			raise Exception("len(delta) != num_nodes")
		self.num_nodes = num_nodes
		self.delta_matrix = delta_matrix 
		if tau_matrix is None:
			self.tau_matrix = []
			for i in range(0, num_nodes):
				self.tau_matrix.append([0] * num_nodes)

	def etha(self, r, s):
		return 1.0 / self.delta_matrix[r][s]

	def update_tau(self, r, s, new_value):
		self.tau_matrix[r][s] = new_value

	def reset_tau(self):
		avg = self.average_delta()
		self.tau0 = 1.0 / (self.num_nodes * 0.5 * avg)
		#print "Average = %s" % (avg,)
		#print "Tau0 = %s" % (self.tau0)
		for r in range(0, self.num_nodes):
			for s in range(0, self.num_nodes):
				self.tau_matrix[r][s] = self.tau0

	def average_delta(self):
		return self.average(self.delta_matrix)

	def average_tau(self):
		return self.average(self.tau_matrix)

	def average(self, matrix):
		sum = 0
		for r in range(0, self.num_nodes):
			for s in range(0, self.num_nodes):
				sum += matrix[r][s]

		avg = sum / (self.num_nodes * self.num_nodes)
		return avg
