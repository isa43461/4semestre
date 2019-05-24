import random
from graphviz import Digraph
import matplotlib.pyplot as plt

random.seed(1107)

g = Digraph('G', filename='ejercicio2.1')

##erdos 
def random_erdos(n,p):
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if random.random()<p:
                E.append((i,j))
    G = [[] for i in range(n)]
    for i,j in E:
        G[i].append(j)
        G[j].append(i)
    return G
###tarjan para sacar puntos de articulación, puentes y num cc
def solve(G):
    global parent,low,visited,depth,suma, Apoint, Puentes, Comp, cont
    n = len(G)
    cont = 0
    Apoint = []
    Puentes = []
    Comp = [1 for _ in G]
    visited = [0 for _ in G]
    parent = [-1 for _ in G]
    depth = [0 for i in range(n)]
    low = [0 for i in range(n)]
    suma = 0
    for u in range(n):
        if(visited[u] == 0):
            dfs(G,u)
            cont += 1

def dfs(G,u):
    global parent,low,visited,depth,Apoint,suma, Puentes, Comp, cont
    low[u] = depth[u] = suma
    suma += 1
    visited[u] = 1
    children= 0
    for v in G[u]:
        if(visited[v] == 0):
            parent[v] = u 
            children += 1
            dfs(G,v)
            low[u] = min(low[u],low[v])
            if(depth[u] < low[v]):
                Puentes.append((u,v))
            if(low[v] >= depth[u] and parent[u] != -1):
                Comp[u] += 1
                Apoint.append(u)
            elif(parent[u] == -1 and children > 1):
                Comp[u] += 1
                Apoint.append(u)
        elif(parent[u] != v):
            low[u] = min(low[u], depth[v])

#lista de adyacencia a lista de arcos para graficar el grafo
#el grafo se grafica con flechas en el Graphviz sin embargo, asegura los 2 sentidos (u,v) y (v,u)
def list2edgelist(G):
    n = len(G)
    E = []
    for i in range(n):
        g.node(str(i))
        for j in G[i]:
            g.edge(str(i),str(j))
    return E

#Average of number of cc
def average(grafo):
    global cont
    numero = len(grafo)
    componentes = cont
    resultado = numero//componentes
    return resultado

#Average degree
def degree(G):
    n = len(G)
    deg = []
    for i in range(n):
        lg = len(G[i])
        deg.append(lg)
    suma1 = sum(deg)
    div = len(deg)
    res = suma1//div
    return res

#tripletas, combinación de len(G[u]) y 2
def tripletas(G):
    n = len(G)
    contTrip = 0 
    for u in range(n):
        contTrip += ((len(G[u]))*(len(G[u])-1)) // 2
    return contTrip

# def trp(G):
#     trp = 0
#     for i in range(len(G)):
#         trp += factorial(len(G[i])) // (factorial(2) * factorial(len(G[i]) - 2))
#     return trp

##lista de adyacencia a matriz
def list2mat(G):
    n = len(G)
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] = 1
    return M

##algoritmo extraido de: https://www.geeksforgeeks.org/number-of-triangles-in-directed-and-undirected-graphs/
def Triangulos(G): 
    n = len(G) 
    Triangulos = 0
    for i in range(n): 
        for j in range(n): 
            for k in range(n): 
                if(i != j and i != k and j != k and G[i][j] and G[j][k] and G[k][i]): 
                    Triangulos += 1
    res = Triangulos//6
    return res

def main():
    global parent,low,visited,depth,Apoint,suma, Puentes, Comp, cont
    grafo = random_erdos(15,0.2)
    #grafo = [[1,2],[0,2],[0,1]]
    solve(grafo)
    mt = list2mat(grafo)
    triang = Triangulos(mt)
    print("Number of connected components: ",cont)
    print("Average size of the connected components: ",average(grafo))
    print("Number of articulation points: ",len(set(Apoint)))
    print("Number of bridges: ",len(Puentes))
    print("Average node degree: ",degree(grafo))
    print("Number of triplets: ",tripletas(grafo))
    print("Number of triangles: ", triang)
    x = list2edgelist(grafo)
    g.view()
main()