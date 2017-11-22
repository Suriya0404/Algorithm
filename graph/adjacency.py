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







