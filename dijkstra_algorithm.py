'''
  *** Dijkstra algorithm
  With you want to look for more details on HOW and WHY, go to the 'dijkstra_simple.py' file,
  it uses a smaller graph and has more comments detailing everything
'''

# Graph
graph = {}
graph["book"] = {}
graph["book"]["lp"] = 5
graph["book"]["poster"] = 0

graph["poster"] = {}
graph["poster"]["bass"] = 30
graph["poster"]["drums"] = 35

graph["lp"] = {}
graph["lp"]["bass"] = 15
graph["lp"]["drums"] = 20

graph["bass"] = {}
graph["bass"]["piano"] = 20

graph["drums"] = {}
graph["drums"]["piano"] = 10

# Cost hash table (Key == node, Value == cost)
cost = {}
cost['book'] = 0
cost['lp'] = float ("inf")
cost['poster'] = float ("inf")
cost['bass'] = float ("inf")
cost['drums'] = float ("inf")
cost['piano'] = float ("inf")

# Parents hash table (The key is the son and the value the parent)
parents = {}

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
    while next_node != "piano":
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
    parent = 'piano'
    while parent != 'book':
        print(parent + " " + "<--" + " ", end='')
        parent = parents[parent]
    print(start)
    print("The total cost is: " + str(cost['piano']))


dijkstra("book")