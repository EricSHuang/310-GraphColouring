"""
CMPT310: a2_q3.py
Eric Huang
"""
from csp import *
from a2_q1 import *
import time

graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
          rand_graph(30, 0.4), rand_graph(30, 0.5)]

rounds = 1 	#set to 5 later
for i in range(0, rounds):
	for j in range(0, 1):	#change to len(graphs) later
		currGraph = graphs[j]

		variables = []
		for node in currGraph:
			variables.append(node)
		domains = list(range(0,len(currGraph)))	#each node could be in any group from 0 to n-1
		neighbors = currGraph
		contraint = different_values_constraint

		csp = CSP(variables, domains,neighbors, contraint)
		#domains = []
		#for key in currGraph:
		#	domains.append(currGraph[key])
		print(csp)

		