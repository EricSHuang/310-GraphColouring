"""
CMPT310: a2_q3.py
Eric Huang
"""
from csp import *
from a2_q1 import *
import time


def run_q3():
    """Uses backtracking_search to provides exact solutions to the random graphs
    created."""

    graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
              rand_graph(30, 0.4), rand_graph(30, 0.5)]
    #graphs = [{0: [1, 2], 1: [0], 2: [0], 3: []}]    #test graph

    numRounds = 5     #set to 5
    for i in range(0, numRounds):
        print("------------------")
        print("*****Round %d*****" %(i+1))
        print("------------------")
        for j in range(0, len(graphs)): #set to len(graphs)
            currGraph = graphs[j]
            startTime = time.time()
            #print(currGraph)

            """---SETTING UP THE CSP---"""
            for k in range(0, len(currGraph)):
                variables = []
                for node in currGraph:
                    variables.append(node)

                domains = {}
                #each node could be in any group from 0 to numVars-1
                for l in range(0, len(currGraph)):
                    #domains[l] = list(range(0, len(currGraph)))
                    domains[l] = list(range(0, k))

                neighbors = currGraph
                constraint = different_values_constraint

                csp = CSP(variables, domains, neighbors, constraint)
                #csp = MapColoringCSP(d2, neighbors)
                #print(csp.variables)
                #print("neighbors: ", csp.neighbors)
                #print("pre ac3: ", csp.domains)
                #print("constraints: ", csp.constraints)
                consistent = AC3(csp)
                if (consistent):
                    #print("GRAPH %d IS CONSISTENT WITH DOMAIN[0, %d]" %(((j * 1) + 0.1), k))
                    #print("post ac3: ", csp.domains)


                    ans = backtracking_search(csp, mrv, lcv, forward_checking)
                    if (ans != None):
                        """ANSWER AND REPORTS"""
                        #print(ans)
                        print("-----Probability %0.1f Graph -----" %((j * 0.1) + 0.1))

                        #Running Time
                        elapsedTime = time.time() - startTime
                        print("Running Time: %f seconds" %(elapsedTime))

                        #Number of Teams
                        numTeams = 0
                        teams = []
                        for l in range(0, len(ans)):
                            if (not contains(teams, ans[l])):
                                teams.append(ans[l])
                                numTeams += 1
                        print("Number of Teams: ", numTeams)

                        #Number of Times CSP variables were assigned and unassigned
                        numAssigned = csp.nassigns
                        numUnassigned = numAssigned - len(currGraph)
                        #every superfluous assignment means that a var was unassigned
                        print("Assignments: %d, Unassignments: %d" %(numAssigned, numUnassigned))

                        #Number of Edges in the Graph (Extra)
                        numEdges = 0
                        for l in range(0, len(currGraph)):
                            numEdges += len(currGraph[l])
                        numEdges = int(numEdges / 2)
                        print("Number of Connections: ", numEdges)

                        #Graph analysis complete (new line for readability)
                        print("\n")
                        break;

        print("\n") #round ended (new-line for readability)


run_q3()
