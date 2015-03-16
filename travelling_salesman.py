import pickle
import sys
import math
import random
import graphbit
import biggroup
import traceback

def main(argv):
	random.seed(227)

	num_cities = int(argv[0])

	if num_cities <= 10:
		num_ants = 20
		num_iterations = 12
		num_repetitions = 1
	else:
		num_ants = 28
		num_iterations = 20
		num_repetitions = 1

	city_data = pickle.load(open(argv[1], "r"))
	city_names = city_data[0]
	distances = city_data[1]
	#why are we doing this?
	if num_cities < len(distances):
		distances = distances[0:num_cities]
		for i in range(0, num_cities):
			distances[i] = distances[i][0:num_cities]



	try:
		graph = graphbit.GraphBit(num_cities, distances)
		best_path_value = None
		best_path_cost = sys.maxint
		for i in range(0, num_repetitions):
#			print "Repetition %s" % i
			graph.reset_tau()
			workers = biggroup.BigGroup(graph, num_ants, num_iterations)
			print "Colony Started"
			workers.start()
			if workers.best_path_cost < best_path_cost:
#				print "Colony Path"
				best_path_value = workers.best_path_value
				best_path_cost = workers.best_path_cost

		print "\n------------------------------------------------------------"
		print "					 Results								"
		print "------------------------------------------------------------"
		print "\nBest path = %s" % (best_path_value,)
		city_vec = []
		for node in best_path_value:
			print city_names[node] + " ",
			city_vec.append(city_names[node])
		print "\nBest path cost = %s\n" % (best_path_cost,)
		results = [best_path_value, city_vec, best_path_cost]
		pickle.dump(results, open(argv[2], 'w+'))
	except Exception, e:
		print "exception: " + str(e)
		traceback.print_exc()


if __name__ == "__main__":
	main(sys.argv[1:])
