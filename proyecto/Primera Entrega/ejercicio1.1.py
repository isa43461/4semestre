import random
from graphviz import Digraph
import matplotlib.pyplot as plt
random.seed(1107)

g = Digraph('G', filename='ejercicio1.1')

def random_erdos(n,p):
    E = []
    for i in range(n):
        for j in range(n):
            if random.random()<p and i != j:
                E.append((i,j))
    G = [[] for i in range(n)]
    for i,j in E:
        G[i].append(j)
    return G

#print(grafo)
#grafo = [[2,3],[0],[1],[4],[]]
#grafo = [[1],[4,5,2],[3,6],[2,7],[0,5],[6],[5],[3,6]]

def dfs(u,num, G):
    global vis, scc
    vis[u] = 1
    scc[u] = num
    for v in G[u]:
        if(vis[v] == 0):
            dfs(v,num, G)
    return

def dfs_list(u):
    global L, vis, I
    vis[u] = 1
    for v in I[u]:
        if(vis[v] == 0):
            dfs_list(v)
    L.append(u)
    return

def compute(G):
    global L,I, scc, vis, cont
    n = len(G)
    scc = [-1 for i in range(n)]

    I = [[] for i in range(n)]
    for i in range(n):
        for j in G[i]:
            I[j].append(i)
    vis = [0 for i in range(n)]
    L = []
    for i in range(n):
        if(vis[i] == 0):
            dfs_list(i)
    vis = [0 for i in range(n)]
    cont = 0
    while(len(L)):
        i = L.pop()
        if(vis[i] == 0):
            dfs(i,cont, G)
            cont += 1

    edges = 0
    for u in range(n):
        for v in G[u]:
            if(scc[u] != scc[v]):
                edges += 1
    return edges

def average(grafo):
    global cont
    numero = len(grafo)
    componentes = cont
    resultado = numero//componentes
    return resultado

def list2edgelist(G):
    n = len(G)
    E = []
    for i in range(n):
        g.node(str(i))
        for j in G[i]:
            g.edge(str(i),str(j))
            #E.append((i,j))
    return 

def main():
    global cont
    grafo = random_erdos(15,0.2)
    sccEdges = compute(grafo)
    print("preambulo 1 (numero de scc): ",cont)
    rs = average(grafo)
    print("preambulo 2 (promedio): ", rs)
    print("preambulo 3 (numero de puentes que conectan scc): ",sccEdges)
    x = list2edgelist(grafo)
    g.view()

main()