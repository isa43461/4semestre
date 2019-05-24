import random
from graphviz import Digraph
import matplotlib.pyplot as plt
##randos rengi
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

##kosajaru
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
##puentes que conectan dos scc
    edges = 0
    for u in range(n):
        for v in G[u]:
            if(scc[u] != scc[v]):
                edges += 1
    return edges
##promedio
def average(grafo):
    global cont
    numero = len(grafo)
    componentes = cont
    resultado = numero//componentes
    return resultado
##funcion para graficar
def graficar(met1,met2,met3, p_small):
    plt.xlabel('p_small')
    plt.ylabel('# resultado')
    plt.plot(p_small,met1,linestyle='-', color='m',label = "Number of SCC")
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met2,linestyle=':', color='r' ,label = "Average size")
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met3,linestyle='--', color='c',label = "Number of edges")
    plt.legend(loc="center right")
    plt.title('Ejercicio 1.2')        
    plt.savefig("TRESMETRICAS.png", bbox_inches='tight')

def main():
    global cont
    p_small = [0,0.005,0.010,0.015,0.020,0.025,0.030,0.035,0.040,0.045,0.050,0.055,0.060,0.065,0.070,0.075,0.080,0.085,0.090,0.095]
    met1 = []
    met2 = []
    met3 = []
    for i in p_small:
        metrica1 = []; metrica2 = [] ; metrica3 = []
        for j in range(200):
            grafo = random_erdos(100,i)
            sccEdges = compute(grafo)
            res = average(grafo)
            metrica1.append(cont)
            metrica2.append(res)
            metrica3.append(sccEdges)
        sumaMet1 = sum(metrica1)
        promedioMet1 = sumaMet1//200
        met1.append(promedioMet1)
        sumaMet2 = sum(metrica2)
        promedioMet2 = sumaMet2//200
        met2.append(promedioMet2)
        sumaMet3 = sum(metrica3)
        promedioMet3 = sumaMet3//200
        met3.append(promedioMet3)
    graficar(met1,met2,met3, p_small)
main()
