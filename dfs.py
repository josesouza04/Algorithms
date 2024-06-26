'''
    Algorithm to traverse a graph using Depth First Search
    Discipline: Algorithms 1 - Federal University of Minas Gerais

    This algorithm calculates the discovery and finish times of each vertex of a graph
'''

class Graph:
    def __init__ (self, n : int):
        self.n = n # number of vertices
        self.adj = [[] for _ in range(n)] # adjacency list
        self.color = ['white' for _ in range(n)] # color of each vertex
        self.pi = [-1 for _ in range(n)] # parent of each vertex
        self.d = [-1 for _ in range(n)] # discovery time
        self.f = [-1 for _ in range(n)] # finish time
        self.globalTime = 0 # global time
    
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
    
def dfs(G : Graph): # to traverse the whole graph
    for u in range(G.__sizeof__()):
        if G.color[u] == 'white':
            dfsVisit(G, u)

def dfsVisit(G : Graph, u : int): 
    G.color[u] = 'gray' # u has been discovered
    G.globalTime += 1
    G.d[u] = G.globalTime
    for vertex in G.adj[u]: # to explore the neighbors of u
        if G.color[vertex] == 'white':
            G.pi[vertex] = u
            dfsVisit(G, vertex)
    G.color[u] = 'black' # u has been finished
    G.globalTime += 1 
    G.f[u] = G.globalTime

def main():
    myGraph = createGraph()
    printGraph(myGraph)

    if myGraph != None:
        dfs(myGraph)
        print('Discovery and finish times: ')
        for i in range(myGraph.__sizeof__()):
            print(f'Vertex {i}: ({myGraph.d[i]}, {myGraph.f[i]})')
    return 0

if __name__ == '__main__':
    main()
