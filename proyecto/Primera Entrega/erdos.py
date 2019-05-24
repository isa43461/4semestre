import random
from graphviz import Digraph
import matplotlib.pyplot as plt
random.seed(1107)

def random_erdos(n,p):
    E = []
    for i in range(n):
        for j in range(n):
            if random.random()<p:
                E.append((i,j))
    G = [[] for i in range(n)]
    for i,j in E:
        G[i].append(j)
    return G

grafo = random_erdos(15,0.2)
print(grafo)

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
    global L,I, scc, vis
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
    return scc

scc = compute(grafo)
print("preambulo 1: ",scc)

def average(grafo, scc):
    numero = len(grafo)
    componentes = len(set(scc))
    print(numero,componentes)
    resultado = numero/componentes
    print("preambulo 2: ", resultado)

average(grafo, scc)

def imprimir(grafo):


#for i,x in enumerate(scc):
#   print(i,x)

hists = []
for ronda in range(100):
    G = random_erdos(20, 0.3)

    n = len(G)
    degs = [len(G[i]) for i in range(n)]
    hist = [0]*n
    for d in degs:
        hist[d]+=1
    hists.append(hist)

hist = [0]*n
for h in hists:
    for i in range(n):
        hist[i]+=h[i]

for i in range(n):
    hist[i]/=len(hists)

print(hist)

plt.stem(hist)
plt.title('Degree distribution')
plt.xlabel('degree')
plt.ylabel('# nodes with a given degree')

#plt.plot([1200*k**-3 if k>=3 else 0 for k in range(n)], color='orange')

plt.show()'''

