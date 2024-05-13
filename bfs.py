'''
    Algorithm to traverse a graph using Breadth First Search
    Discipline: Algorithms 1 - Federal University of Minas Gerais

    This algorithm calculates the minimum distance between two vertices of a graph
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
    def __init__ (self, n : int):
        self.n = n # number of vertices
        self.adj = [[] for _ in range(n)] # adjacency list
        self.color = ['white' for _ in range(n)] # color of each vertex
        self.pi = [-1 for _ in range(n)] # parent of each vertex
        self.d = [-1 for _ in range(n)] # discovery time
        self.q = Queue() # queue of discovered vertices
    
    def __sizeof__(self):
        return self.n
    
    # auxiliary funcion for creating the graph
    def addEdge(self, u : int, v : int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def existsEdge(self, u : int, v : int):
        return v in self.adj[u]

    def isComplete(self):
        for u in range(self.n):
            if len(self.adj[u]) != self.n - 1:
                return False
        return True

def createGraph():
    try:
        n = int(input('Enter the number of vertices: '))
        if n < 0: 
            raise ValueError
        elif n == 0: 
            return None
        G = Graph(n)
        print('Now, enter the edges of the graph (u, v) - (to finish, enter -1 -1): ')
        while True:
            if G.isComplete():
                print('Graph is complete.')
                break
            u, v = map(int, input().split())
            if u < -1 or v < -1: 
                print('Invalid edge. Try again.')
            elif u == -1 and v == -1: 
                break
            elif G.existsEdge(u, v):
                print('Edge already exists. Try again.')
            elif u >= n or v >= n:
                print('Invalid edge. Try again.')
            else: 
                G.addEdge(u, v)
        return G
    except ValueError:
        print('Invalid input. Try again.')
        return createGraph()
    except Exception as e:
        print('An error occurred. Try again.')
        return createGraph()

def printGraph(G: Graph):
    for u in range(G.__sizeof__()):
        print(u, end = ' -> ')
        for v in G.adj[u]:
            print(v, end = ' ')
        print()

'''
for vertex u: 
    if it is white, it has not been visited yet
    if it is gray, it has not been finished yet
    if it is black, it has been finished 
'''

def bfs(G: Graph, s : int):
    for u in range(G.__sizeof__()):
        if u != s:
            G.color[u] = 'white'
            G.d[u] = -1
            G.pi[u] = -1
    G.color[s] = 'gray'
    G.d[s] = 0
    G.pi[s] = -1
    G.q.enqueue(s)
    while not G.q.isEmpty():
        u = G.q.head()
        for v in G.adj[u]:
            if G.color[v] == 'white':
                G.color[v] = 'gray'
                G.d[v] = G.d[u] + 1
                G.pi[v] = u
                G.q.enqueue(v)
        G.q.dequeue()
        G.color[u] = 'black'

def distance(G: Graph, s : int, t : int):
    bfs(G, s)
    if G.d[t] == -1:
        return 'There is no path from', s, 'to', t
    return G.d[t]
    
def main():
    myGraph = createGraph()
    printGraph(myGraph)
    s, t = map(int, input('Enter the vertices to calculate the distance: ').split()) 
    print('Distance is', distance(myGraph, s, t))
    return 0

if __name__ == '__main__':
    main()
