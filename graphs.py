from collections import defaultdict

# class Grahps:
#     def __init__(self):
#         self.graphs = defaultdict(list)
#
#
#     def insertedge(self,v1,v2):
#         self.graphs[v1].append(v2)
#         self.graphs[v2].append(v1)
#
#     def printgraphs(self):
#         for node in self.graphs:
#             for val in self.graphs[node]:
#                 print(node,'=>',val)
#
# g = Grahps()
# g.insertedge(1,5)
# g.insertedge(5,100)
# g.insertedge(5,2)
# g.insertedge(2,7)
# g.insertedge(7,1)
#
# g.printgraphs()

#graph adjenct matrix

#
# class Graph:
#     def __init__(self,numberofNodes):
#         self.numberofNodes = numberofNodes+1
#         self.graph = [[0 for x in range(numberofNodes+1)]
#                         for y in range(numberofNodes+1)]
#
#     def withinBounds(self,v1,v2):
#         return (v1 >= 0 and v1 < self.numberofNodes) and (v2 >=0 and v2 <=self.numberofNodes)
#
#     def insertEdge(self,v1,v2):
#         if (self.withinBounds(v1,v2)):
#             self.graph[v1][v2]= 1
#             self.graph[v2][v1]=1
#
#
#     def printGraph(self):
#         for i in range(self.numberofNodes):
#             for j in range(len(self.graph[i])):
#                 if self.graph[i][j]:
#                     print(i,'=>',j)
#
#
# g = Graph(5)
# g.insertEdge(1,2)
# g.insertEdge(2,3)
# g.insertEdge(4,5)
#
# g.printGraph()

#BFS graph

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def setEgde(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited = set()
        queue =[]
        queue.append(s)
        visited.add(s)

        while(queue):
            u = queue.pop(0)
            print(u,end=" ")

            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

g = Graph()
g.setEgde(2,1)
g.setEgde(2,5)
g.setEgde(5,6)
g.setEgde(5,8)
g.setEgde(6,9)
g.bfs(2)