"""
Vertex - node
payload - additional information on node
edge - connects two node.
directed graph or digraph - edges are one directional
weight - edge are weighted (cost)
graph G = (V,E)
V - set of vertices and E - set of edges
subgraph s
Cycle n directed graph -> path starts and end in same node
directed graph with no cycle is called acyclic graph (DAG)

Adjacency Matrix:
easiest way to implement graph using 2d array
row and column represent vertex and cell represent edge (weight)
Requires more space

Adjacency list:
id = v0
adj = { v5:2, v1:3 } vector followed by weight - space efficient

"""


class Vertex:
    """ Vertex class
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, key, weight=0):
        """ Add neighbor to vertex """
        self.connectedTo[key]=weight

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id) + ' is connected to ' + str([x for x in self.connectedTo.keys()])

    def getWeight(self,id):
        return self.connectedTo[id]

    def getConnections(self):
        return self.connectedTo.keys()


class Graph:
    def __init__(self):
        self.vertexList ={}
        self.numVertex = 0

    def addVertex(self, key):
        self.numVertex += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self,key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, n):
        return n in self.vertexList.keys()

    def addEdge(self,s,t,w):
        if s not in self.vertexList:
            self.addVertex(s)
        if t not in self.vertexList:
            self.addVertex(t)

        self.getVertex(s).addNeighbor(t, w)



def buildGraph():
    d = {}
    g = Graph()

    with open('/Users/suriya0404/data/word.txt', 'r') as f1:
        for word in f1:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]

                if bucket not in d:
                    d[bucket] = [word]
                else:
                    d[bucket].append('word')

    for buc in bucket:
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g





if __name__ == '__main__':
    g = Graph()

    # Adding vertices
    for i in range(6):
        g.addVertex(i)

    print(g.getVertices())

    # Adding edge for vertex 0 and 1 with weight of 10
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 20)
    g.addEdge(3, 4, 100)

    for v in g:
        print(v)
        print(v.getConnections())
        print('\n')

    buildGraph()

    g.print()



