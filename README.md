# Graph Algorithms

I'm currently studying some algorithms with the book "Grokking Algorithms".<br>
Right now, I'm into GRAPHS. So this repository is for study purposes only.

(Although I would prefer C-language, I'm using Python because I want to focus on the algorithm itself and not to worry about memory management)<br>
# Graphs
Graphs are structure models to study the relation between objects. The objects are represented by vertices (nodes) and each of them are connected by an edge. Graphs can be undirected/directed (ordered/unordered) and weighted/unweighted, which means:
- Direction: The graph is directed when its relationship between objects has order.<Br>
A---->B is directed because A points to B but B doesn't point to A.<Br>A-----B (or A<---->B) is undirected which means that the relation between those are bidirectional<br>
Fictional exemple: Nodes: People | Edges: Love<br>
Bob---->Ane means that Bob loves Ane but Ane does not love Bob<br>
Bob----Ane here both love each other
- Weight: Edges can have weight to represent one more "variable" in the system. One general use for graphs is to calculate the distance between two nodes, if the edges are unweighted so the shortest path will be the one with less edges to pass by.<Br>
However, if the system is weighted and the edges has values (i.e.: km or minutes), then the shortest path is the one with the lowest value of the SUM of weights.<br>
Example: You want to go from A to B in your city. You can follow two paths:<br>
1- Pass through four streets<br>
2- Pass through eight streets<Br>
Can you answer what is the best option? No because we don't know how long are each street, even if option 1 has less streets to pass by, this doesn't mean too much if they are too long when comparing to the streets of the option 2. The answer of this question would be solved calculating the SUM of distance/time of each street per option.<Br>
(**IMPORTANT: I don't know if it is the best way but in both exercises I'm using dictionaries (hash tables) to build the graphs, where each node is a key to values, values which are the vertices connected to the key node. Those values connected to the key node can be a key on their own too and have their own values)
<p align="center">
  <img 
    width="400"
    height="300"
    src="https://media.geeksforgeeks.org/wp-content/uploads/minmEdges-1.png"
  >
  <p align="center">Graph, nodes and edges - Undirected & Unweighted</p><br>
</p>
<p align="center">
  <img 
    width="400"
    height="400"
    src="https://www.techiedelight.com/wp-content/uploads/weighted-edges.png"
  >
  <p align="center">Graph - WEIGHETED and DIRECTED</p>
</p><br>

<hr><br>

## graph.py (Breadth-first search (BFS))
<br>
This first study is the most basic graph search algorithm, the Breadth-first search (BFS) looks for an specific object in an UNDIRECTED (unordered) and UNWEIGHTED GRAPH.<Br><Br>

Problem: I want to find a book seller<Br>
Solution: Ask to my friends if they sell books, if not -> then ask to the friends of my friends and so on. <br>
<p align="center">
  <img 
    width="500"
    height="350"
    src="https://drek4537l1klr.cloudfront.net/bhargava/Figures/101fig02.jpg"
  >
  <p align="center">One of these nodes is the book seller</p>
</p>
Each friend will be a node, and two nodes connected by an edge means that they are friends

Abstraction: MyFriends = [Bob, Carl, John], John_Friends = [Linda, Carol]... each of my friends have more friends, and each of their friend's friends 
have even more friends.
So I'm basically asking to everyone that has a connection with someone that I know.

Example: John----Linda. John and Linda are vertices connected by an edge, which means that they are friends

Besides finding a seller, I want to find the closest one. So buying from my friend is better than buying from my friend's friend

(I highly recommend you to look for graph images in order to better understand)<br><br><hr><br>
## dijkstra_algorithm.py (Dijkstra Algorithm)
<br>
The Dijkstra Algorithm is used to find the shortest path between two nodes in an WEIGHTED (only positive values) and DIRECTED graph.<br><br>
How does it work?<Br><Br>
1- From the start chosen point, go to the cheapest neighbor (which the start point is directing). Let's say that you went from "Start" to "B", which is the cheapest path, but there was the node "A" as an option too.<br>
2- Now, you will do the same thing for B, go to the next cheapest neighbor. However, you'll also update the cost values of each node. Let's say that from B you can go to A, if the path Start-->B-->A is cheaper than Start-->A, the algorithm must update the cost of A.<Br><br>
This was a real basic explanation but let me enter in code details:<Br>
The program needs a hash table for the graph itself, and inside this hash table there will be other hash tables for each node, being the key a node-parents and the value is the weight, i.e.: graph["start"]["b"] = 6 means that from START node to B node, there is a edge with weight 6.<br>
Also, it is needed a hash table for COSTS to mantain the total cost to go to a certain node updated.<br>
And a PARENTS hash table, this is what will give us the final path, the parent-node must be always the cheapest one.<br><br>
Now, let's go to the exercise itself, the dijkstra_algorithm.py:<br><Br>
Bob is in a thrift store where people can exchange items betweem themselves. Bob has a book and wants to buy a Piano. To get the piano Bob has to have or a Bass-Guitar or a Drum-Set, and to have those things Bob has first to have a Rare-LP or a Poster.<br>
So Bob will have to make some trades. As you can see in the image, besides the item itself, Bob will have to pay something more to exchange items. Example, if Bob trade his Book for the Rare-LP, he'll also have to give $5 more for it.<br>
<br>
So the question is: which path is the cheapest? Which one Bob will spend less money?<br><Br>
The answer is: Book --> LP --> Drum --> Piano<br> This is the cheapest path which he'll spend $35 to get the piano.<Br><br>
<p align="center">
  <img 
    width="500"
    height="350"
    src="https://drek4537l1klr.cloudfront.net/bhargava/Figures/123fig02.jpg"
  >
  <p align="center">Start point: Book || End Point: Piano</p>
</p>
<Br><br>

## dijkstra_simple.py (Dijkstra Algorithm)
<br>
In this exercise, a simpler graph was used as you can see in the image.<br><br>
<p align="center">
  <img 
    width="400"
    height="300"
    src="https://drek4537l1klr.cloudfront.net/bhargava/Figures/116fig03.jpg"
  >
  <p align="center">Shortest path from Start to End?</p>
</p>
Here is easier to know the shortest path. The answer is:<br>
Start --> B --> A --> End || Total cost for this path: 6<br><Br>
If you choose other paths:<br>
Start --> A --> End || Total cost: 7<Br>
Start --> B --> End || Total cost: 7
