from sys import stdin
from collections  import deque
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

def solve(G):
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
			cont +=	1
	return cont

def main():
	people, relations = map(int, stdin.readline().strip().split())
	diccionario = dict()
	while(people != 0 or relations != 0):
		for i in range(people):
			names = stdin.readline().strip()
			diccionario.update({names : i})
		G = [ [] for i in range(people)]
		for i in range(relations):
			friend1 = stdin.readline().strip()
			friend2 = stdin.readline().strip()
			num1 = diccionario.get(friend1)
			num2  = diccionario.get(friend2)
			G[num1].append(num2)
		x = solve(G)
		print(x)
		people, relations = map(int, stdin.readline().strip().split())
main()