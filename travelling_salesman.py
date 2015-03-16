import pickle
import sys
import math
import random
import graphbit
import biggroup
import traceback

def main(argv):
	#seeding random number generator
	random.seed(227)

	num_cities = int(argv[0])

	#decides parameters based on number of cities specified
	if num_cities <= 10:
		num_ants = 20
		num_iterations = 12
		num_repetitions = 1
	else:
		num_ants = 28
		num_iterations = 20
		num_repetitions = 1

	#loads names and distances between cities
	city_data = pickle.load(open(argv[1], "r"))
	city_names = city_data[0]
	distances = city_data[1]

	#confines the array of city distances to the number 
	if num_cities < len(distances):
		distances = distances[0:num_cities]
		for i in range(0, num_cities):
			distances[i] = distances[i][0:num_cities]
	try:
		#initialise tau and delta arrays
		graph = graphbit.GraphBit(num_cities, distances)
		best_path_value = None
		best_path_cost = sys.maxint
		for i in range(0, num_repetitions):
			print "Started colony %s" % i
			#resets tau after every iteration
			graph.reset_tau()
			#initialise group of workers
			workers = biggroup.BigGroup(graph, num_ants, num_iterations)
			#start testing
			workers.start()
			if workers.best_path_cost < best_path_cost:
				#print "Colony Path"
				best_path_value = workers.best_path_value
				best_path_cost = workers.best_path_cost

		print "\n------------------------------------------------------------"
		print "	                 Results                                "
		print "------------------------------------------------------------"
		print "\nBest path = %s" % (best_path_value,)
		city_vec = []
		for node in best_path_value:
			print city_names[node] + " ",
			city_vec.append(city_names[node])
		print "\nBest path cost = %s\n" % (best_path_cost,)
		#save results to file
		results = [best_path_value, city_vec, best_path_cost]
		pickle.dump(results, open(argv[2], 'w+'))
	except Exception, e:
		print "exception: " + str(e)
		traceback.print_exc()


if __name__ == "__main__":
	main(sys.argv[1:])
