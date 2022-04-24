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
graph['start']['b'] = 2

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
cost['start'] = 0
cost["end"] = float ("inf")
cost['a'] = float ("inf")
cost['b'] = float ("inf")

# copy of cost hash table. But this one will have nodes deleted
tobeupdated_nodes = dict(cost)

# Function to return the lowest weight node from the COST hash table
def lowest_weight():
    key = None
    return min(tobeupdated_nodes, key = tobeupdated_nodes.get)

# Dijkstra algorithm to find the shortest path
def dijkstra(start):

    # Next node (the lowest weight)
    next_node = start
    path_cost = 0

    # Updating costs and parents for each node
    while next_node != "end":
        if next_node in tobeupdated_nodes.keys():
            for neighbor in graph[next_node]:
                if cost[neighbor] > path_cost + graph[next_node][neighbor]:
                    cost[neighbor] = graph[next_node][neighbor] + path_cost
                    tobeupdated_nodes[neighbor] = graph[next_node][neighbor] + path_cost
                    parents[neighbor] = next_node
            tobeupdated_nodes.pop(next_node, None)
            previous_node = next_node
            next_node = lowest_weight()
            if next_node in graph[previous_node]:
              path_cost += graph[previous_node][next_node]
            else:
              path_cost = cost[next_node]

    # Printing result
    print("The best path is: ", end='')
    parent = 'end'
    while parent != 'start':
        print(parent + " " + "<--" + " ", end='')
        parent = parents[parent]
    print(start)
    print("The total cost is: " + str(cost['end']))


dijkstra("start")

