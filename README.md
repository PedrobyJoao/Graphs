# Graph Algorithms

I'm currently studying some algorithms with the book "Grokking Algorithms".<br>
Right now, I'm into GRAPHS. So this repository is for study purposes only.<br><hr>
### Graphs
are structure models to study the relation between objects. The objects are represented by vertices (nodes) and each of them are connected by an edge. Graphs can be ordered/unordered and weighted/unweighted.
<hr>

## graph.py (Breadth-first search (BFS))
<br>
This first study is the most basic graph search algorithm, the Breadth-first search (BFS) looks for an specific object in an undirected graph.<Br><Br>

Problem: I want to find a book seller<Br>
Solution: Ask to my friends if they sell books, if not -> then ask to the friends of my friends and so on. <br>

Each friend will be a node, and two nodes connected by an edge means that they are friends

Abstraction: MyFriends = [Bob, Carl, John], John_Friends = [Linda, Carol]... each of my friends have more friends, and each of their friend's friends 
have even more friends.
So I'm basically asking to everyone that has a connection with someone that I know.

Example: John----Linda. John and Linda are vertices connected by an edge, which means that they are friends

Besides finding a seller, I want to find the closest one. So buying from my friend is better than buying from my friend's friend

(I highly recommend you to look for graph images in order to better understand)<br>
<hr><br>
(Although I'd prefer C-language, I'm using Python because I want to focus on the algorithm itself and not to worry about memory management with 'malloc' and 'free')
