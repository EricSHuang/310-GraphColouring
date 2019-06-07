"""
CMPT310: a2_q2.py
Eric Huang
"""
from csp import *


def check_teams(graph, csp_sol):
    """Returns True if csp solution dictionary 'csp_sol' satisfies all the
    constraints in the friendship graph, and False otherwise."""

    #Not all nodes assigned to a group
    if (len(graph) != len(csp_sol)):
        return False

    #Check that connected nodes aren't in the same group
    groups = {}
    #Assign nodes to their respective group
    for node, group in csp_sol.items():
        if group in groups:     #Checks if the group already exists
            hold = groups[group]
            hold.append(node)
            groups[group] = hold
        else:
            groups[group] = [node]
    #print(groups)

    for group in groups:
        currGroup = groups[group]
        #print(currGroup)
        for i in range(0, len(currGroup)):
            connections = graph[currGroup[i]]   #i-th node's friends
            for j in range(0, len(currGroup)):
                if (contains(connections, currGroup[j])):
                    return False
    return True



def contains(arr, x):
"""Returns true if array 'arr' contains element 'x'"""
    for element in arr:
        if (element == x):
            return True
    return False



#Test Cases
g1 = {0: [1, 2], 1: [0], 2: [0], 3: []}
ans1 = {0:0, 1:1, 2:1, 3:0}

g2 = {0: [3], 1: [3, 4], 2: [4], 3: [1, 4], 4: [1, 3]}
ans2 = {0:0, 1:0, 2:0, 3:1, 4:2}
wrongAns2 = {0:0, 1:0, 2:0, 3:1, 4:1}

g3 = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
ans3 = {0:0, 1:1, 2:2, 3:3}

g4 = {0: [], 1: [], 2: []}
ans4 = {0:0, 1:0, 2:0}

#print(check_teams(g2, wrongAns2))
