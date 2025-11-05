class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            devertex = queue.pop(0)
            print(devertex)
            for adjustment in self.gdict[devertex]:
                if adjustment not in visited:
                    visited.append(adjustment)
                    queue.append(adjustment)
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjust in self.gdict[popVertex]:
                if adjust not in visited:
                    visited.append(adjust)
                    stack.append(adjust)

customDict = {"a":["b","c"],
              "b":["a","d","g "],
              "c":["a","e"],
              "d":["b","e","e"],
              "e":["d","f","c"],
              "f":["d","e"]
                  }

graph = Graph(customDict)
graph.dfs('a')