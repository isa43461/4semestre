class segmentTree:
	def __init__(self, A):
		hojas = 1
		while hojas < len(A):
			hojas*=2
		self.tree = [0 for _ in range(2*hojas)]
		self.tree[0] = 'BASURA'
		for i in range(len(A)):
			self.tree[i+hojas] = A[i]
		for i in reversed(range(1,hojas)):
			self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
		self.hojas = hojas
		return
	def suma(self,lo,hi, i = 1):
		if lo==hi:
			ans = 0
		else:
			ans = self._suma(lo,hi,i=1,L=0 ,R = self.hojas)
		return ans
	def _suma(self, lo,  hi, i, L, R):
		M = (L+R)//2
		if(L == lo and R == hi):
			ans = self.tree[i]
			#print("1",ans)
		elif(hi<= M):
			ans = self._suma(lo,hi,2*i,L,M)
			#print("2",ans)
		elif(lo >= M):
			ans = self._suma(lo,hi,2*i+1,M,R)
			#print("3",ans)
		else:
			ans = self._suma(lo,M,2*i,L,M)
			#print("4",ans)
			ans = max(ans, self._suma(M,hi,2*i+1,M,R))
			#print("5",ans)
		return ans
	def set(self, i, val):
		i = i+self.hojas
		self.tree[i] = val
		while i!=1:
			pa = i//2
			self.tree[pa] = max(self.tree[2*pa] , self.tree[2*pa+1])
			i = pa
		return

A = [2,3,5,-1,1]
S = segmentTree(A)
print(S.suma(0,5))
S.set(4,20)
print(S.suma(2,5))
