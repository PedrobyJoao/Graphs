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

 * Now we have all information about nodes, their neighbors and the weights of each edge between two vertices
 * We have now to create the PARENTS-TABLE so that we know which is the lowest weight edge
 * Example, TO the node 'A' there are two paths: 'B' and 'Start', we will have to update the parents of A accordinly to the weight,
 always looking for the lowest one.

'''

# Parents hash table (The key is the son and the value the parent)
parents = {}

# array of updated nodes
updated_nodes = []

# Function to compare the weights between two paths and return the cheapest one
def lowest_weight():
    print("")

# Dijkstra algorithm to find the shortest path


print(graph[0])