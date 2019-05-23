from sys import stdin

class dforest(object):
  def __init__(self, size=10):
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 1 for _ in range(size) ]
  
  def find(self, x):
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    fx,fy = self.find(x),self.find(y)
    if fx!=fy:
      rx,ry = self.__rank[fx],self.__rank[fy]
      if rx>ry:
        self.__parent[fy] = fx
      else:
        self.__parent[fx] = fy
        if rx==ry:
          self.__rank[fy] += 1
          
def kruskal(graph, lenv):
  ans = list()
  graph.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  while i!=len(graph):
    u,v,d = graph[i]
    if df.find(u)!=df.find(v):
      #ans.append((u, v, d))
      df.union(u, v)
    else: ans.append(d)
    i += 1
 # assert df.ccount()==1
 # assert df.csize(df.find(0))==lenv
  return ans

def printf(x):
  if(len(x) == 0): print("forest")
  else:
    for i in x:
      print(i, end = " ")
    print()

def main():
  n,m = map(int, stdin.readline().strip().split())
  while(n > 0 or m > 0):
    G = []
    while(m > 0):
      u,v,w = map(int, stdin.readline().split())
      G.append((u, v, w))
      m -= 1
    x = kruskal(G, n)
    printf(x)
    n,m = map(int, stdin.readline().strip().split())
main()