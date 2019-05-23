from heapq import heappush, heappop
from sys import stdin
INF = float('inf')

def solve():
	global n,m,b,p,G,B,P,dist,queue
	ans = INF
	visited = [ False for _ in range(n)]
	parent = [None for _ in range(n)]
	while (len(queue)!= 0):
		d,u = heappop(queue)
		if(visited[u] == False):
			visited[u] = True
			for v,w in G[u]:
				duv = d+w
				if(visited[v] == False and dist[v]>duv):
					dist[v] = duv
					parent[v] = u
					heappush(queue, (duv,v))
	return dist

def main():
	global n,m,b,p,G,B,P,dist,queue
	letters = stdin.readline().strip().split()
	while(len(letters) != 0):
		n = int(letters[0]); m = int(letters[1]); b = int(letters[2]); p = int(letters[3])
		#print("num",n,m,b,p)
		G = [[] for _ in range(n)]
		for i in range(m):
			u,v,w = map(int, stdin.readline().split())
			G[u].append((v,w))
			G[v].append((u,w))
		B = [int(x) for x in stdin.readline().strip().split()]
		#print(B)
		if(p != 0):
			P = [int(x) for x in stdin.readline().strip().split()]
		#print(P)
		dist = [INF for _ in range(n)]
		queue = []
		if(p != 0):
			for i in P:
				dist[i] = 0
				heappush(queue, (0,i))
		ans = solve()
		#print(ans)
		r = []
		for j in B:
			r.append(ans[j])
		#print(B)
		mx = max(r)
		#print()
		time, r1 = 0, []
		for j in range(len(r)):
			if(r[j] == mx):
				time += 1
				r1.append(B[j])
		#print("res",r1)
		r1.sort()
		if(mx != INF): print(time, end = ' '); print(mx)
		else: print(time, end = ' '), print("*")
		for i in r1:
			print(i, end = " ")
		print()
		letters = stdin.readline().strip().split()
main()