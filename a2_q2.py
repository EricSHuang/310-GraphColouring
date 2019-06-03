"""
CMPT310: a2_q2.py
Eric Huang
"""
from csp import *

def check_teams(graph, csp_sol):
    #Not all nodes assigned to a group
    if (len(graph) != len(csp_sol)):
        return False

    #Check that connected nodes aren't in the same group

    #this section seems unnecessary
    groups = {}
    #Assign nodes to their respective group
    for node, group in csp_sol.items():
        #hold = groups[group]
        #hold.append(node)
        #groups[group] = hold
        #groups[group].append(node)
        groups[group] = node

    print(groups)
    return True
"""
    for group in groups:
        currGroup = groups[group]
        for i in range(0, len(currGroup)):
            connections = graph[currGroup[i]]
            for j in range(0, len(currGroup)):
                if (contains(connections, j)):
                    return False
"""




#Returns true if array 'arr' contains element 'x'
def contains(arr, x):
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

print(check_teams(g1, ans1))
