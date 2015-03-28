import pickle
import sys
import math
import graphbit
import biggroup
import traceback
import parameters

def main(argv):

	num_cities = int(argv[0])

	#decides parameters based on number of cities specified
	if num_cities <= parameters.cutoff:
		num_ants = parameters.num_ants_small
		num_iterations = parameters.num_iterations_small
		num_repetitions = parameters.num_repetitions_small
	else:
		num_ants = parameters.num_ants_big
		num_iterations = parameters.num_iterations_big
		num_repetitions = parameters.num_repetitions_big

	#loads names and distances between cities
	city_data = pickle.load(open(argv[1], "r"))
	city_names = city_data[0]
	distances = city_data[1]

	#confines the array of city distances to the number of cities chosen
	if num_cities < len(distances):
		distances = distances[0:num_cities]
		for i in range(0, num_cities):
			distances[i] = distances[i][0:num_cities]
	try:
		#initialise tau and delta arrays
		graph = graphbit.GraphBit(num_cities, distances)
		best_path_vector = None
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
				best_path_vector = workers.best_path_vector
				best_path_cost = workers.best_path_cost
		print "\n------------------------------------------------------------"
		print "	                 Results                                "
		print "------------------------------------------------------------"
		print "\nBest path = %s" % (best_path_vector,)
		city_vector = []
		for node in best_path_vector:
			print city_names[node] + " ",
			city_vector.append(city_names[node])
		print "\nBest path cost = %s\n" % (best_path_cost,)
		#save results to file
		results = [best_path_vector, city_vector, best_path_cost]
		pickle.dump(results, open(argv[2], 'w+'))
	except Exception, e:
		print "exception: " + str(e)
		traceback.print_exc()


if __name__ == "__main__":
	main(sys.argv[1:])
