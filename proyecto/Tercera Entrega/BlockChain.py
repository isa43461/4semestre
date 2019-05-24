import random
from graphviz import Digraph
import matplotlib.pyplot as plt
import numpy as np
#from tqdm import tqdm
random.seed(1107)

def delay(t,p):
 	tp = np.random.exponential(p)
 	res = t - tp
 	if(res < 0):
 		res = 0 
 	return res

def padre(G, TF):
	aux1 = [0,0,0] 
	p = 0; prof = 0
	for k in range(len(G)):
		if(G[k][0] <= TF):
			if(G[k][2] == aux1[2] and G[k][0] < aux1[0]):
				p = k; prof = (G[k][2])
				aux1[0] = G[k][0]
				aux1[1] = G[k][1]
				aux1[2] = G[k][2]
			elif(G[k][2] > aux1[2]):
				p = k; prof = (G[k][2])
				aux1[0] = G[k][0]
				aux1[1] = G[k][1]
				aux1[2] = G[k][2]			
	return p, prof
def blockChain(n,p):
	t = np.random.exponential(1.0)
	G = [[0,0,0]]
	for i in range(n):
		t+=np.random.exponential(1.0)
		TF = delay(t,p)
		pd, profu = padre(G, TF)
		profu = profu+1
		aux = [t,pd, profu]
		G.append(aux)
	return G

def graficar(met1,met2,p):
    plt.xlabel('p')
    plt.ylabel('# resultado')
    plt.plot(p,met1,linestyle="-", color='m',label = "profMax")     
    plt.ioff()
    plt.ion() 
    plt.plot(p,met2,linestyle="-", color='c',label = "bloques perdidos") 
    plt.legend(loc="center right")
    plt.title('Ejercicio 3.1')        
    plt.savefig("met12.png", bbox_inches='tight')
    plt.close()

def graficarPtiendeAINF(met1,met2,p):
    plt.xlabel('p')
    plt.ylabel('# resultado')
    plt.plot(p,met1,linestyle="-", color='m',label = "profMax")     
    plt.ioff()
    plt.ion() 
    plt.plot(p,met2,linestyle="-", color='c',label = "bloques perdidos") 
    plt.legend(loc="upper right")
    plt.title('Ejercicio 3.1')        
    plt.savefig("pInf.png", bbox_inches='tight')
    plt.close()

def profMax(block):
	global maximo
	maximo = 0
	for j in range(len(block)):
		if(maximo < block[j][2]):
			maximo = block[j][2]
	return maximo

def main():
	global maximo
	p = [float("%.2f" % ((0.05)*i)) for i in range(41)]
	#pInf = [float("%.2f" % ((0.5)*i)) for i in range(101)]
	met1 = [] ; met2 = []; n = 1000; m = 200
	for i in p:
		metrica1 = 0 ; metrica2 = 0;
		for h in range(m):
			block = blockChain(n,i)
			metrica1 += profMax(block)
			metrica2 += ((len(block)-1)-maximo)
		met1.append(metrica1//m)
		met2.append(metrica2//m)
	graficar(met1, met2, p)
	#graficarPtiendeAINF(met1, met2, p)
	#print(p)
	#print(blockChain(5, 0.05))
main()