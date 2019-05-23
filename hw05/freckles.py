from heapq import heappush, heappop
from sys import stdin
import math

class dforest(object):
  def __init__(self, size=10):
    self.parent = [ i for i in range(size) ]
    self.rank = [ 1 for _ in range(size) ]
  
  def find(self, x):
    if self.parent[x]!=x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, x, y):
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.rank[fx],self.rank[fy]
      if rx>ry:
        self.parent[fy] = fx
      else:
        self.parent[fx] = fy
        if rx==ry:
          self.rank[fy] += 1
          
def kruskal(graph, lenv):
  ans = 0
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      ans += d
      df.union(u, v)
    i += 1
  return ans
  
def main():
	cases = int(stdin.readline())
	while(cases > 0):
		space = stdin.readline()
		freckles = int(stdin.readline())
		G = []
		for i in range(freckles):
			x,y = map(float, stdin.readline().split())
			G.append((x,y))
		dist = 0
		p = []
		for j in range(freckles):
			for k in range(j+1, freckles):
				x1 = G[j][0]
				y1 = G[j][1]
				x2 = G[k][0]
				y2 = G[k][1]
				dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
				if(dist != 0):
					p.append((j,k,dist))
		acum = kruskal(p,freckles)
		print("%.2f" % acum)
		if(cases > 1):
			print()
		cases -=1
main()