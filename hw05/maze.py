from heapq import heappush, heappop
from sys import stdin
INF = float('inf')

# def solve():
# 	global N, E, G
# 	ans = INF
# 	visited = [ False for _ in range(N)]
# 	parent = [None for _ in range(N)]
# 	dist = [INF for _ in range(N)]
# 	queue, dist[E] = [(0, E)], 0
# 	while (len(queue)!= 0):
# 		d,u = heappop(queue)
# 		if(visited[u] == False):
# 			visited[u] = True
# 			for v,w in G[u]:
# 				duv = d+w
# 				if(visited[v] == False and dist[v]>duv):
# 					dist[v] = duv
# 					parent[v] = u
# 					heappush(queue, (duv,v))
# 	return dist


def main():
	global N,E,G
	cases = int(stdin.readline())
	while(cases > 0):
		space = stdin.readline()
		N = int(stdin.readline())
		E = int(stdin.readline())
		E = E-1
		T = int(stdin.readline())
		M = int(stdin.readline())
		G = [[] for i in range(N)]
		for i in range(M):
			u,v,d = map(int, stdin.readline().split())
			v = v-1
			u = u-1
			G[v].append((u,d))
		ans = solve()
		l = len(ans)
		mouse = 0
		for k in range(l):
			if(ans[k] <= T):
				mouse +=1
		print(mouse)
		if(cases > 1):
			print("")
		cases -=1
main()