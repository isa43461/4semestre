import random
from graphviz import Digraph
import matplotlib.pyplot as plt

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

def graficar(met2):
    plt.xlabel('p_small')
    plt.ylabel('# resultado')
   # plt.plot(met1)
    #plt.ioff()
    #plt.ion() 
    plt.plot(met2)
    plt.ioff()
    plt.ion() 
    #plt.plot(met3)
    #plt.plot(met1, label = "Number of SCC")
    plt.plot(met2, label = "Average size")
    #plt.plot(met3, label = "Number of edges")
    plt.legend()
    plt.legend(loc="center right")     
    plt.title('Ejercicio 1.2')        
    plt.savefig("segundaDerivada.png", bbox_inches='tight')

def average(grafo):
    global cont
    numero = len(grafo)
    componentes = cont
    resultado = numero/componentes
    return resultado

def busquedaBinaria(lista, x):
    print(x)
    print(len(lista))
    l, h = 0 ,len(lista)-1
    while(l+1 != h):
        print(l,h)
        mid = (l+h)//2 
        if(x < lista[mid]): h = mid
        else: l = mid
    return l,h

def main():
    global cont
    p_small = [0,0.005,0.010,0.015,0.020,0.025,0.030,0.035,0.040,0.045,0.050,0.055,0.060,0.065,0.070,0.075,0.080,0.085,0.090,0.095]
    met3 = []; met2 = []
    for i in p_small:
        metrica3 = []; metrica2 = []
        for j in range(200):
            grafo = random_erdos(100,i)
            sccEdges = compute(grafo)
            metrica3.append(sccEdges)
            res = average(grafo)
            metrica2.append(res)
        sumaMet2 = sum(metrica2)
        promedioMet2 = sumaMet2//200
        met2.append(promedioMet2)            
        sumaMet3 = sum(metrica3)
        promedioMet3 = sumaMet3//200
        met3.append(promedioMet3)
    primeraDerivada = []
    #print(met2)
    for k in range(1,20):
        m = (met2[k] - met2[k-1])/(p_small[k] - p_small[k-1])
        primeraDerivada.append(m)
    segundaDerivada = []
    for l in range(1,19):
        m1 = (primeraDerivada[l] - primeraDerivada[l-1])/(p_small[l] - p_small[l-1])
        segundaDerivada.append(m1)
    #print(primeraDerivada)
    print(segundaDerivada)
    positivos = []; negativos = []
    # for i in segundaDerivada:
    #     if(i < 0):
    #         negativos.append(i)
    #     elif(i > 0):
    #         positivos.append(i)
    # NumIzq = max(negativos)
    # NumDer = min(positivos)
    # print(NumIzq, NumDer)
    # #low,hi = busquedaBinaria(segundaDerivada, minimo)
    # graficar(segundaDerivada)
    #lw = met3[x-1]; hi = met3[x+1]
    #dx = (hi-lw)/20
    #listaX = [0.010 + (dx*i) for i in range(20)] 
main()
