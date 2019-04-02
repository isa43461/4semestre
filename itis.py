import sys
from collections  import deque

x = []
def next_int():
	global i, s
	while not s[i].isdigit() and s[i] != '-':
		i += 1
	j = i+1
	while j < len(s) and s[j].isdigit():
		j+=1
	ans = int(s[i:j])
	i = j
	return ans

def solve3(A):		## si tira true es arbol sino, el grafo tiene un ciclo
	global indeg, m, x
	topo = []
	band3 = True
	indeg0 = [ l for l in range(m) if indeg[l] == 0]
	while(len(topo) < m):
		if(len(indeg0) == 0):
			band3 = False
			return band3
		else:
			h = indeg0.pop()
			topo.append(h)
			for j in A[h]:
				indeg[j] -= 1
				if(indeg[j] == 0):
					indeg0.append(j)
	return band3

def solve(A):
	global indeg, contt, m, x
	band = True
	m = len(A)
	vis = [0 for _ in range(m)]
	indeg = [0 for _ in range(m)]
	indeg0 = [ l for l in range(m) if indeg[l] == 0]
	for u in range(m):
		for v in A[u]:
			indeg[v] += 1
			if(u == v):
				band = False
	cont1 = 0
	for i in range(m):
		if(indeg[i] == 0): #raiz
			cont1 += 1
			x = i
		if(indeg[i] > 1):
			band = False
	if(cont1 != 1):
		band = False
	if len(indeg) == 0:
		return True
	return band

def main():
	global i, s, indeg, contt
	s,i = sys.stdin.read(), 0
	a, b = next_int(), next_int()
	contt = 0 
	while(a>=0 or b >= 0):
		E = []
		diccionario = dict()
		cont = 0
		while a > 0 or b > 0:
			if a not in diccionario:
				diccionario[a] = cont; cont += 1
			if b not in diccionario:
				diccionario[b] = cont; cont += 1
			E.append((a,b))
			a,b = next_int(), next_int()
		A = [[] for _ in range(cont)]
		for n in E:
			num1 = diccionario.get(n[0])
			num2  = diccionario.get(n[1])
			A[num1].append(num2)
		res = solve(A)
		res1 = solve3(A)
		contt +=1
		if(res == True and res1 == True):
			print("Case", contt, "is a tree.")
		else:
			print("Case", contt, "is not a tree.")
		a,b = next_int(), next_int()
main()