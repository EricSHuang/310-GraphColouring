# Map Colouring Problem
## Function
Finds the chromatic number of a graph using backtrack search and min conflicts
local search. <br>
Every node must be coloured such that they do not share the same colour with
any of their neighbors. How many colours do you need to colour the graph?<br>
Using the Ice Breaker Problem analogy, we are assigning people into groups where
no one is prior friends with anyone else on their team.

## Files
**a2_q1.py** creates random graphs with n nodes numbered 0 to n-1
where every pair of nodes is connected with a probability p. <br>
**a2_q2.py** checks if given solutions satisfy all the constraints. In other words,
every node is assigned a team, and no nodes in a team are connected. <br>
**a2_q3.py** finds the exact solution to the problem using *back tracking search*.
The solutions it provides are the lowest number of colours/teams required. <br>
**a2_q4.py** finds an approximate solution using the *min conflict algorithm*.
When the number of nodes becomes large, finding the exact solution will take a
long time. Approximate solutions are acceptable sometimes, and save a lot of time.


## Context and Credits
Completed as an assignment for CMPT310: Artificial Intelligence Survey <br>
csp.py, search.py, and utils.py are courtesy of https://github.com/aimacode/aima-python
