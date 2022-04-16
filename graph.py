'''
Problem: I want to find a book seller
Solution: Ask to my friends if they sell books, if not -> then ask to the friends of my friends and so on

Abstraction: MyFriends = [Bob, Carl, John], John_Friends = [Linda, Carol]... each of my friends have more friends, and each of their friend's friends 
have even more friends.
So I'm basically asking to everyone that has a connection with someone that I know.

To this, I will use GRAPHS, which is information (ordered or unordered) represented by EDGES and VERTICES.
Each vertice is someone/something and the edges make the connection between the vertices. In our case,
a vertice will be a person, and the connection(edge) means that they are friends.
Example: John----Linda. John and Linda are vertices connected by an edge, which means that they are friends

Besides finding a seller, I want to find the closest one. So buying from my friend is better than buying from my friend's friend

(I highly recommend you to look for graph images in order to better understand)
'''
from collections import deque

# Creating the graphs itself with fictional data, each vertice is a person who can be a book seller
graph = {}
graph["me"] = ["linda", "john", "paul"] # My friends
graph["linda"] = ["jenny", "mikasa", "eren"] # linda's friends
graph["john"] = ["bob", "lee", "kim"] # john's friends
graph["paul"] = ["liam", "noah", "oliver"] # paul's friends
# All bellow do not have friends =/
graph["jenny"] = []
graph["mikasa"] = []
graph["eren"] = []
graph["bob"] = []
graph["lee"] = []
graph["kim"] = []
graph["liam"] = []
graph["noah"] = []
graph["oliver"] = []
# I have 3 friends, and each of them have more 3, so I'll search for the book seller between 12 people

book_seller = input("Choose some of them to be the book seller: ")

# Function to verify if the person is the book seller
def verify(person):
    if person == book_seller:
        return True
    return False

def find_seller(me):
    tobe_verified = deque()
    tobe_verified += graph[me]
    while tobe_verified:
        person = tobe_verified[0]
        tobe_verified.popleft()
        if verify(person) == True:
            print("The seller is: "+person)
            return person
        tobe_verified += graph[person]
    return print("The name that you provided is not the seller =/")

find_seller("me")
        
