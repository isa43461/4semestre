from sys import stdin
from collections  import deque

def solve(G):
	global parent,low,visited,depth,suma, Apoint, Puentes
	n = len(G)
	Apoint = []
	Puentes = []
	visited = [0 for _ in G]
	parent = [-1 for _ in G]
	depth = [0 for i in range(n)]
	low = [0 for i in range(n)]
	suma = 0
	for u in range(n):
		if(visited[u] == 0):
			dfs(G,u)

def dfs(G,u):
	global parent,low,visited,depth,Apoint,suma, Puentes
	low[u] = depth[u] = suma
	suma += 1
	visited[u] = 1
	children = 0
	for v in G[u]:
		if(visited[v] == 0):
			parent[v] = u 
			children += 1
			dfs(G,v)
			low[u] = min(low[u],low[v])
			if(low[v] >= depth[u] and parent[u] != -1):
				Apoint.append(u)
			elif(parent[u] == -1 and children > 1):
				Apoint.append(u)
		else:
			low[u] = min(low[u], depth[v])
def main():
	global nodos, Apoint, suma, Puentes
	nodos = int(stdin.readline())
	while(nodos != 0):
		G = [set() for i in range(nodos)]
		lista = [int(x) for x in stdin.readline().split()]
		while(lista[0] != 0):
			point = lista[0]-1
			for i in range(1,len(lista)):
				G[point].add(lista[i]-1)
				G[lista[i]-1].add(point)
			lista = [int(x) for x in stdin.readline().split()]
		solve(G)
		x = set(Apoint)
		print(len(x))
		print(low)
		nodos = int(stdin.readline())
main()