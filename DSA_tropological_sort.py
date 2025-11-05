from collections import defaultdict
class Graph:
    def __init__(self,numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdges(self,vertices,edges):
        self.graph[vertices].append(edges)

    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k ,visited,stack)

        print(stack)

customGraph = Graph(8)
customGraph.addEdges("a","c")
customGraph.addEdges("c","e")
customGraph.addEdges("e","h")
customGraph.addEdges("e","f")
customGraph.addEdges("f","g")
customGraph.addEdges("b","d")
customGraph.addEdges("b","c")
customGraph.addEdges("d","f")

customGraph.topologicalSort()