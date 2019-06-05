"""
CMPT310: a2_q3.py
Eric Huang
"""
from csp import *
from a2_q1 import *
import time


def run_q3():
    graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3),
              rand_graph(100, 0.4), rand_graph(100, 0.5)]
    #graphs = [{0: [1, 2], 1: [0], 2: [0], 3: []}]    #test graph

    numRounds = 2     #set to 5
    for i in range(0, numRounds):
        print("------------------")
        print("*****Round %d*****" %(i+1))
        print("------------------")
        for j in range(0, len(graphs)):
            currGraph = graphs[j]
            startTime = time.time()
            #print(currGraph)

            """---SETTING UP THE CSP---"""
            variables = []
            for node in currGraph:
                variables.append(node)

            domains = {}
            #each node could be in any group from 0 to numVars-1
            for k in range(0, len(currGraph)):
                domains[k] = list(range(0, len(currGraph)))

            neighbors = currGraph
            constraint = different_values_constraint

            #csp = CSP(variables, domains, neighbors, constraint)
            csp = MapColoringCSP(domains, neighbors)
            #print(csp.variables)
            #print("neighbors: ", csp.neighbors)
            #print("pre ac3: ", csp.domains)
            #print("constraints: ", csp.constraints)
            consistent = AC3(csp)
            if (not consistent):
                print("GRAPH %d WAS NOT CONSISTENT" %(j))
                break;
            #print("post ac3: ", csp.domains)

            """ANSWER AND REPORTS"""
            ans = min_conflicts(csp)
            print("-----Probability %0.1f Graph -----" %((j * 0.1) + 0.1))

            #Running Time
            elapsedTime = time.time() - startTime
            print("Running Time: %f seconds" %(elapsedTime))

            #Number of Teams
            numTeams = 0
            teams = []
            for k in range(0, len(ans)):
                if (not contains(teams, ans[k])):
                    teams.append(ans[k])
                    numTeams += 1
            print("Number of Teams: ", numTeams)

            #Number of Times CSP variables were assigned and unassigned
            numAssigned = csp.nassigns
            numUnassigned = len(currGraph) - numAssigned
            #every superfluous assignment means that a var was unassigned
            print("Assignments: %d, Unassignments: %d" %(numAssigned, numUnassigned))

            #Number of Edges in the Graph (Extra)
            numEdges = 0
            for k in range(0, len(currGraph)):
                numEdges += len(currGraph[k])
            numEdges = int(numEdges / 2)
            print("Number of Connections: ", numEdges)

            #Graph analysis complete (new line for readability)
            print("\n")

        print("\n") #round ended (new-line for readability)


run_q3()