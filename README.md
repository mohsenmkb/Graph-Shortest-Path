# Graph-Shortest-Path


This algorithm takes the data of a directed graph from a CSV file and can calculate the shortest path between any pair of nodes. The algorithm uses operations research tools for modeling the graph, and the objective function attempts to minimize the sum of the edge weights that the path contains. We use the Gurobi solver with Pyomo as the problem is a mixed-integer programming one.

The results of the algorithm are saved in the "report.txt" file.


Graph image (Networkx):
![alt text](https://raw.githubusercontent.com/mohsenmkb/Graph-Shortest-Path/main/routes.png "Graph image 1")
