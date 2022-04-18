'''
Problem: I want to go from the point START to the point END, the edges have weight and are directed.
            The path should be the shortest!
Solution: Dijkstra Algorithm

Dijkstra Algorithm is a graph algorithm made for weighted (positive values only), it returns the shortest path
between two points.

Again, the graph will be build with hash tables (dict in python)
'''

# Building the main graph
# Each node has their own hash table, inside the main hash table graph, to represent the weights
graph = {} # main hash table

# hash table for the START node where it will be stored weight values of edges
graph['start'] = {} 
graph['start']['a'] = 6
graph['start']['b'] = 0

# hash table for the B node
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

# hash table for the A node (there is no directed edge from A to B, just from B to A)
graph['a'] = {}
graph['a']['end'] = 1

# hash table for the END node
graph['end'] = {}

'''

 * Now we have all information about the nodes, their neighbors and the weights of each edge between two vertices
 * We have now to create the PARENTS-TABLE so that we know which is the shortest path through the parents, which are based on the lowest weight
 * We also have to create a COST-TABLE to keep track and make updates of the lowest weight-cost to get to a node

'''

# Parents hash table (The key is the son and the value the parent)
parents = {}

# Cost hash table (Key == node, Value == cost)
cost = {}

# array of updated nodes
updated_nodes = []

# Function to compare the weights between two paths and return the cheapest one
def lowest_weight(node):
    lowest_weight = float ("inf")
    lowest_node = None
    for key in graph[node]:
        if graph[node][key] < lowest_weight:
            lowest_weight = graph[node][key]
            lowest_node = key
    return lowest_node, lowest_weight

# Dijkstra algorithm to find the shortest path
def dijkstra():
    next_node = lowest_weight("start")[0]
    for path in graph[next_node]:
        graph[next_node][path] = 
    print("Teste")

for i in graph['b']:
    print(i)