from sys import stdin
import time 
start_time = time.time()

cx = [-1,0,1,1,1,0,-1,-1]
cy = [1,1,1,0,-1,-1,-1,0]

def next(a,b,A):
    r = []
    for i in range(len(cx)):
        if(0 <= a + cx[i] < len(A) and 0 <= b + cy[i] < len(A[0]) and A[a + cx[i]][b + cy[i]] == A[a][b]):
            r.append([a + cx[i],b + cy[i]])
    return r

def dfs(k,l, M, A,e):
    q = []
    q.append((k,l))
    while(len(q)):
        u,t = q.pop()
        for v,i in next(u,t,A):
            if(M[v][i] == 0):
                M[v][i] = e
                q.append((v,i))    
    return M
        
def solve(A):
    fl = len(A)
    cl = len(A[0])
    M = []
    for i in range(fl):
        M.append([])
        for j in range(cl):
            M[i].append(0)
    cont = 1
    for k in range(fl):
        for l in range(cl):
            if(M[k][l] == 0):
                M[k][l]=cont
                M = dfs(k,l,M,A,cont)
                cont += 1
                
    return M

def imprimir(n):
    ans = None
    if(n < 10): ans = 1
    elif(n < 100): ans = 2
    elif(n < 1000): ans = 3
    elif(n < 10000): ans = 4
    elif(n < 100000): ans = 5
    return ans

def imprimir2(dfs):
    Lst = []
    fl = len(dfs)
    cl = len(dfs[0])
    for j in range(cl):
        ans = 0
        for i in range(fl):
            if(ans < dfs[i][j]):
                ans = dfs[i][j]
        Lst.append(ans)
    new = []
    for i in range(len(Lst)):
        x = imprimir(Lst[i])
        new.append(x)
    for i in range(fl):
        for j in range(cl):
            print(str(dfs[i][j]).rjust(new[j]), end = '')
            if(j+1 != cl):
                print(" ", end = '')
        print()
    print('%', end = '')    
    print()
def main():
    global columnas, filas
    lista = stdin.readline().strip().split()
    A = []
    while(len(lista)):
        A.append(lista)
        if(lista[0] == '%'):
            A.pop()
            dfs = solve(A)
            A = []
            imprimir2(dfs)
        lista = stdin.readline().strip().split()
        if(len(lista) == 0):
            dfs = solve(A)
            imprimir2(dfs)
main()
