class GraphBit:
	def __init__(self, num_nodes, delta_matrix, tau_matrix=None):
		if __debug__:
			print len(delta_matrix)
		#ensures the size of the array matches the expected number of nodes
		if len(delta_matrix) != num_nodes:
			raise Exception("Number of nodes does not match size of array")
		self.num_nodes = num_nodes
		self.delta_matrix = delta_matrix
		if tau_matrix is None:
			self.tau_matrix = []
			for i in range(0, num_nodes):
				self.tau_matrix.append([0] * num_nodes)

	#returns a variable defined by delta
	def eta(self, r, s):
		return 1.0 / self.delta_matrix[r][s]

	#resets tau when a new iteration starts
	def reset_tau(self):
		average = self.average(self.delta_matrix)
		self.tau0 = 1.0 / (self.num_nodes * 0.5 * average)
		if __debug__:
			print "Average = %s" % (average,)
			print "Tau0 = %s" % (self.tau0)
		for r in range(0, self.num_nodes):
			for s in range(0, self.num_nodes):
				self.tau_matrix[r][s] = self.tau0

	#finds the average value of an array
	def average(self, matrix):
		sum = 0
		for r in range(0, self.num_nodes):
			for s in range(0, self.num_nodes):
				sum += matrix[r][s]
		average = sum / (self.num_nodes * self.num_nodes)
		return average
