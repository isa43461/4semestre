from sys import stdin
from collections  import deque

cx = [-1,1,2,2,1,-1,-2,-2]
cy = [2,2,1,-1,-2,-2,-1,1]
cx2 = [-1,0,1,1,1,0,-1,-1]
cy2 = [1,1,1,0,-1,-1,-1,0]


def next2(a,b,A):
    r = []
    for i in range(len(cx2)):
        if(0 <= a + cx2[i] < len(A) and 0 <= b + cy2[i] < len(A[0])):
            r.append([a + cx2[i],b + cy2[i]])
    return r

def bfs(A, coordenadasA, coordenadasB):
    q = deque()
    q.append(coordenadasA)
    cont = 0
    A[coordenadasA[0]][coordenadasA[1]] = cont
    while(len(q)):
        u,t = q.popleft()
        if(cont == A[u][t]):
            cont += 1
        for v,i in next2(u,t,A):
            if (A[v][i] == 'B'):
                return cont
            if(A[v][i] == '.'):
                A[v][i] = cont
                q.append((v,i))    
                
    return -1

def next(a,b,A):
    for i in range(len(cx)):
        if(0 <= a + cx[i] < len(A) and 0 <= b + cy[i] < len(A[0])):
            if(A[a + cx[i]][b + cy[i]] == '.'):
                A[a + cx[i]][b + cy[i]] = 'C'
    return A

def main():
    cnt = int(stdin.readline())
    for k in range(1,cnt+1):
        lista = stdin.readline().strip().split()
        num1,num2 = map(int,lista)
        A = []
        for n in range(1,num1+1):
            l = list(stdin.readline().strip())
            A.append(l)
        for i in range(num1):
            for j in range(num2):
                if(A[i][j] == 'Z'):
                    A[i][j] = 'C'
                    c = next(i,j,A)
                elif(A[i][j] == 'A'):
                    coordenadasA = (i,j)
                elif(A[i][j] == 'B'):
                    coordenadasB = (i,j)
    
        h = bfs(A,coordenadasA, coordenadasB)
    
        if(h == -1): print("King Peter, you can't go now!")
        else:
            print("Minimal possible length of a trip is",h)
        
main()
