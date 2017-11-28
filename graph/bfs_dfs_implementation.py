from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisted = 1    # white
    visted = 2      # Black
    visiting = 3    # Gray

class node:
    def __init__(self, num):
        self.num = num
        self.state = State.unvisted
        self.adjacency = OrderedDict()

    def __str__(self):
        return str(self.num)

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):


