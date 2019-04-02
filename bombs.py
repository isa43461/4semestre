from sys import stdin
import sys
sys.setrecursionlimit(100000)
def solve(G):
	global parent,low,visited,depth,suma, Apoint, Puentes, Pal
	n = len(G)
	Apoint = []
	Puentes = []
	Pal = [1 for _ in G]
	visited = [0 for _ in G]
	parent = [-1 for _ in G]
	depth = [0 for i in range(n)]
	low = [0 for i in range(n)]
	suma = 0
	for u in range(n):
		if(visited[u] == 0):
			dfs(G,u)

def dfs(G,u):
	global parent,low,visited,depth,Apoint,suma, Puentes, Pal
	low[u] = depth[u] = suma
	suma += 1
	visited[u] = 1
	children= 0
	for v in G[u]:
		if(visited[v] == 0):
			parent[v] = u 
			children += 1
			dfs(G,v)
			if(low[v] >= depth[u] and parent[u] != -1):
				Pal[u] += 1
				Apoint.append(u)
			elif(parent[u] == -1 and children > 1):
				Pal[u] += 1
				Apoint.append(u)
			low[u] = min(low[u],low[v])
		else:
			low[u] = min(low[u], depth[v])

def main():
	global Apoint, a, b, Pal
	a, b = map(int, stdin.readline().strip().split())
	while(a > 0 or b > 0):
		x, y = map(int, stdin.readline().strip().split())
		G = [[] for i in range(a)]
		while x >= 0 or y >= 0:
			G[x].append(y) # son bidireccionales, c va a d y d va a c 
			G[y].append(x) 
			x, y = map(int, stdin.readline().strip().split())
		solve(G)
		#print(G)
		#x = list(set(Apoint))
		lista = []
		mayor = 0
		pos = 0
		for i in range(b):
		    for j in range(a):
		        if(Pal[j] > mayor):
		            mayor = Pal[j]
		            pos = j
		    Pal[pos] = -1
		    lista.append((pos,mayor))
		    mayor = 0
		for i in range(len(lista)):
		    print(lista[i][0],lista[i][1])
		a, b = map(int, stdin.readline().strip().split())
		print()

main()