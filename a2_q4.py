"""
CMPT310: a2_q3.py
Eric Huang
"""
from csp import *
from a2_q1 import *
import time


def run_q4():
    """Uses the min_conflicts algorithm to find an approximate solution.
    min_conflicts runs faster than backtracking_search so it could be used on larger n"""
    
    graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3),
              rand_graph(100, 0.4), rand_graph(100, 0.5)]
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
            for k in range(1, len(currGraph)):
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
                #consistent = True
                if (consistent):
                    #print("GRAPH %0.1f IS CONSISTENT WITH DOMAIN[0, %d]" %(((j * 0.1) + 0.1), k))
                    #print("post ac3: ", csp.domains)


                    ans = min_conflicts(csp, 1000)
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
                        numUnassigned = 0
                        #min_conflicts does not unassign vars, just reassigns them
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


run_q4()
