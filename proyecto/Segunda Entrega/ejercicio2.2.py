import random
from graphviz import Digraph
import matplotlib.pyplot as plt
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

def graficar(met2,met3, met4 , met5, p_small):
    plt.xlabel('p_small')
    plt.ylabel('# resultado')
    plt.plot(p_small,met2,linestyle=':', color='r' ,label = "Average size of CCs")
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met3,linestyle='--', color='c',label = "Number of Art Point")
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met4,linestyle='-.', color='b',label = "Number of bridges")  
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met5,linestyle='--', color='y',label = "Average of degree")      
    plt.legend(loc="center right")
    plt.title('Ejercicio 2.2')        
    plt.savefig("metricas.png", bbox_inches='tight')
    plt.close()

def graficar2(met1,met6,met7, psmUpLr):
    plt.xlabel('psmUpLr')
    plt.ylabel('# resultado')
    plt.plot(psmUpLr,met1,linestyle= "-", color='r' ,label = "Number of CCs")
    plt.ioff()
    plt.ion() 
    plt.plot(psmUpLr,met6,linestyle="-", color='c',label = "Number of Triplets")
    plt.ioff()
    plt.ion() 
    plt.plot(psmUpLr,met7,linestyle="-", color='m',label = "Number of Triangles")      
    plt.legend(loc="center right")
    plt.title('Ejercicio 2.2')        
    plt.savefig("metricas167.png", bbox_inches='tight')
    plt.close()

def graficar3(coc,psmUpLr):
    plt.xlabel('psmUpLr')
    plt.ylabel('# resultado')
    plt.plot(psmUpLr,coc,linestyle="-", color='m',label = "Cociente")      
    plt.legend(loc="center right")
    plt.title('Ejercicio 2.2')        
    plt.savefig("cociente.png", bbox_inches='tight')
    plt.close()

def main():
    global parent,low,visited,depth,Apoint,suma, Puentes, Comp, cont
    p_small = [0,0.005,0.010,0.015,0.020,0.025,0.030,0.035,0.040,0.045,0.050,0.055,0.060,0.065,0.070,0.075,0.080,0.085,0.090,0.095]
    p_large = [float("%.2f" % (0.1 + (0.05*i))) for i in range(19)]
    ##p_small U p_large
    psmUpLr = p_small + p_large
    met1 = [] ; met2 = [] ; met3 = []; met4 = []; met5 = []; met6 = []; met7 = []
    for i in p_small:
        metrica2 = [] ; metrica3 = []; metrica4 = []; metrica5 = []
        for j in range(200):
            grafo = random_erdos(100,i)
            solve(grafo)
            res = average(grafo)
            dg = degree(grafo)
            AP = len(set(Apoint))
            PS = len(Puentes)
            metrica2.append(res)
            metrica3.append(AP)
            metrica4.append(PS)
            metrica5.append(dg)
        sumaMet2 = sum(metrica2)
        promedioMet2 = sumaMet2//200
        met2.append(promedioMet2)
        sumaMet3 = sum(metrica3)
        promedioMet3 = sumaMet3//200
        met3.append(promedioMet3)
        sumaMet4 = sum(metrica4)
        promedioMet4 = sumaMet4//200
        met4.append(promedioMet4)
        sumaMet5 = sum(metrica5)
        promedioMet5 = sumaMet5//200
        met5.append(promedioMet5)
    graficar(met2,met3, met4 , met5, p_small)
    coci = []
    for k in psmUpLr:
        metrica1 = [] ; metrica6 = []; metrica7 = []; cociente = [];
        for l in range(200):
            grafo1 = random_erdos(20,k)
            grafo2 = random_erdos(100,k)
            solve(grafo2)
            cc = cont
            trp = tripletas(grafo1)
            mt = list2mat(grafo1)
            triang = Triangulos(mt)
            cos = 0
            if(trp != 0): 
                cos = triang/trp
            metrica1.append(cc)
            metrica6.append(trp)
            metrica7.append(triang)
            cociente.append(cos)
        sumaCoc = sum(cociente)
        promedioCoc = sumaCoc/200
        coci.append(promedioCoc)
        sumaMet1 = sum(metrica1)
        promedioMet1 = sumaMet1//200
        met1.append(promedioMet1)
        sumaMet6 = sum(metrica6)
        promedioMet6 = sumaMet6//200
        met6.append(promedioMet6)
        sumaMet7 = sum(metrica7)
        promedioMet7 = sumaMet7//200
        met7.append(promedioMet7)
    graficar3(coci,psmUpLr)
    graficar2(met1,met6, met7, psmUpLr)
main()
