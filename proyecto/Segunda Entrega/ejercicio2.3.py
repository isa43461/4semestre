import random
import matplotlib.pyplot as plt
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

def graficaMet34(met3, met4 ,p_small):
    plt.xlabel('p_small')
    plt.ylabel('# resultado')
    plt.plot(p_small,met3,linestyle= "-", color='r' ,label = "Number of Articulation Points")
    plt.ioff()
    plt.ion() 
    plt.plot(p_small,met4,linestyle="-", color='c',label = "Number of Bridges")  
    plt.legend(loc="center right")
    plt.title('Ejercicio 2.3')        
    plt.savefig("metricas34.png", bbox_inches='tight')
    plt.close()
def main():
    global parent,low,visited,depth,Apoint,suma, Puentes, Comp, cont
    p_small = [0,0.005,0.010,0.015,0.020,0.025,0.030,0.035,0.040,0.045,0.050,0.055,0.060,0.065,0.070,0.075,0.080,0.085,0.090,0.095]
    p_large = [float("%.2f" % (0.1 + (0.05*i))) for i in range(19)]
    ##p_small U p_large
    psmUpLr = p_small + p_large
    met1 = []; met3 = []; met4 = []
    for i in p_small:
        metrica3 = []; metrica4 = []
        for j in range(1000):
            grafo = random_erdos(100,i)
            solve(grafo)
            AP = len(set(Apoint))
            PS = len(Puentes)
            metrica3.append(AP)
            metrica4.append(PS)
        sumaMet3 = sum(metrica3)
        promedioMet3 = sumaMet3//200
        met3.append(promedioMet3)
        sumaMet4 = sum(metrica4)
        promedioMet4 = sumaMet4//200
        met4.append(promedioMet4)
    for k in psmUpLr:
        metrica1 = []
        for l in range(1000):
            grafo2 = random_erdos(100,k)
            solve(grafo2)
            cc = cont
            metrica1.append(cc)
        sumaMet1 = sum(metrica1)
        promedioMet1 = sumaMet1//200
        met1.append(promedioMet1)
    graficaMet34(met3,met4 ,p_small)

main()