from sys import stdin
from collections  import deque

uno = [1,10,100,1000]
nueve = [9,90,900,9000]

def states(u):
    ans = []
    for i in range(4):
        if(u // uno[i] % 10 != 9):
            ans1 = u + uno[i]
            ans.append(ans1)
        else:
            ans1 = u - nueve[i]
            ans.append(ans1)
        if(u // uno[i] % 10 != 0):
            ans1 = u - uno[i]
            ans.append(ans1)
        else:
            ans1 = u + nueve[i]
            ans.append(ans1)
    return ans    

states1 = [states(n) for n in range(10000)]
#states1 = [states(8056)]

def bfs(inicio, posicionFinal, vis):
    q = deque()
    q.append(inicio)
    if(vis[inicio] == 2 or vis[posicionFinal] == 2):
        return -1
    vis[posicionFinal] = 'F'
    cont = 0
    vis[inicio] = cont
    print(states1[8056])
    while(len(q)):
        u = q.popleft()
        if(cont == vis[u]):
            cont += 1
        for v in states1[u]:
            if(vis[v] == 'F'):
                return cont
            if(vis[v] == 0):
                vis[v] = cont
                q.append(v)    
    return -1

def main():
    n = int(stdin.readline())
    visitados = [0 for i in range(10000)]
    while(n != 0):
        linea = stdin.readline()
        inicio = int(stdin.readline().replace(" ", ""))
        final = int(stdin.readline().replace(" ", ""))
        numPro = int(stdin.readline())
        vis = visitados.copy()
        for i in range(numPro):
            l = int(stdin.readline().replace(" ", ""))
            vis[l] = 2
        if(inicio == final):
            print(0)
        else:
            print(bfs(inicio,final, vis))
        n -= 1
main()
