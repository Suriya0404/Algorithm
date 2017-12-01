from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisted = 1    # white
    visted = 2      # Black
    visiting = 3    # Gray

class Node:
    def __init__(self, num):
        self.num = num
        self.state = State.unvisted
        self.adjacency = OrderedDict()  # Key: node and value: weight

    def __str__(self):
        return str(self.num)

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()      # key: node and value: adjacent nodes

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)

        if dest not in self.nodes:
            self.add_node(dest)

        # source is type of Node class
        # dest is type of Node class
        # Node class has the property adjacency which is a order dict
        # Edge connect between two nodes and adjacency property stores the connected nodes.
        self.nodes[source].adjacency[self.nodes[dest]] = weight

if __name__ == '__main__':
    g = Graph()

    g.add_edge(0, 1, 5)
    g.add_edge(1, 2, 10)

    print(g.nodes)