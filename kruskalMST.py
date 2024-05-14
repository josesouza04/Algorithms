'''
    Implementation of Minimum Spanning Tree Algorithm
    Discipline: Algorithms 1 - Federal University of Minas Gerais

    Kruskal's Algorithm
'''

class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self, x):
        self.q.append(x)
    
    def dequeue(self):
        if len(self.q) == 0:
            return None
        x = self.q.pop(0)
    
    def head(self):
        if len(self.q) == 0:
            return None
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0

class Graph:
    def __init__(self, n : int = 0):
        self.length = n
        self.adj = [[] for _ in range(n)]
        self.weight = [] # (u, v, w)
        self.totalWeight = 0
    
    def addVertex(self, vertex):
        self.adj.append([])
        self.length += 1

    def removeVertex(self, vertex):
        self.adj.pop(vertex)
        self.length -= 1
    
    def addEdge(self, u, v, w = 1):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.weight.append((u, v, w))
        self.totalWeight += w

    def removeEdge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)
        self.weight.remove((u, v, self.weight[self.weight.index((u, v, 0))][2]))

    def existsEdge(self, u, v):
        return v in self.adj[u]
    
    def isComplete(self):
        for u in range(self.length):
            if len(self.adj[u]) != self.length - 1:
                return False
        return True
    
    def isConnected(self):
        color = bfs(self, 0)
        for u in range(self.length):
            if color[u] == 'white':
                return False
        return True
    
    def printGraph(self):
        for u in range(self.length):
            print(u, end=' -> ')
            for v in self.adj[u]:
                print(v, end=' ')
            print()

def bfs(G: Graph, s : int):
    color = ['white' for _ in range(G.length)]
    d = [-1 for _ in range(G.length)]
    pi = [-1 for _ in range(G.length)]
    q = Queue()
    for u in range(G.length):
        if u != s:
            color[u] = 'white'
            d[u] = -1
            pi[u] = -1
    color[s] = 'gray'
    d[s] = 0
    pi[s] = -1
    q.enqueue(s)
    while not q.isEmpty():
        u = q.head()
        for v in G.adj[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                d[v] = d[u] + 1
                pi[v] = u
                q.enqueue(v)
        q.dequeue()
        color[u] = 'black'

    return color

def partition(weight, left, right):
    pivot = weight[right]
    i = left - 1
    for j in range(left, right):
        if weight[j] <= pivot:
            i += 1
            weight[i], weight[j] = weight[j], weight[i]
    weight[i + 1], weight[right] = weight[right], weight[i + 1]
    return i + 1

def quickSort(weight, left, right):
    if left < right:
        pivot = partition(weight, left, right)
        quickSort(weight, left, pivot - 1)
        quickSort(weight, pivot + 1, right)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        else:
            # u and v are already in the same set, adding this edge would form a cycle
            return False

def detect_cycle(edges, n):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True  # Cycle detected
    return False  # No cycle detected

class MST(Graph):
    def __init__(self, n : int = 0):
        super().__init__()
    
    def removeLoops(self):
        for u in range(self.length):
            if self.existsEdge(u, u):
                self.removeEdge(u, u)
    
    def removeParallelEdges(self):
        for u in range(self.length):
            for v in self.adj[u]:
                if self.adj[v].count(u) > 1:
                    self.removeEdge(u, v)

    def kruskalMST(self):
        self.removeLoops()
        self.removeParallelEdges()
        edges = []
        quickSort(self.weight, 0, len(self.weight) - 1)
        for edge in self.weight:
            u, v, w = edge
            if not self.existsEdge(u, v):
                self.addEdge(u, v, w)
                edges.append((u, v))
                self.totalWeight += w
            if detect_cycle(edges, self.length):
                self.removeEdge(u, v)
                self.totalWeight -= w
        return self.totalWeight

def main():
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
        (5, 6, 3),
        (6, 7, 1),
        (7, 8, 8),
        (8, 9, 7),
        (9, 10, 2),
        (10, 11, 4),
        (11, 12, 5),
        (12, 13, 6),
        (13, 14, 3),
        (0, 14, 10),
        (2, 11, 12),
        (4, 10, 7),
        (7, 13, 2)
    ]
    numVertices = 15

    myMST = MST(numVertices)
    for u, v, w in edges:
        myMST.addEdge(u, v, w)
    myMST.printGraph()

    return 0

if __name__ == '__main__':
    main()