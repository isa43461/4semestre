from sys import stdin
from collections  import deque

abc = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

def solve(lista):
    ad = [[] for i in range(26)] 
    long, i = len(lista)-1, 1
    q = deque()
    q.append(lista[0])
    while(i < long):
        rep = q.pop()
        if(rep == lista[i]):
            ult = q.pop()
            for j in range(26):
                if(ult == abc[j]):
                    ad[j].append(rep)
                if(rep == abc[j]):
                    ad[j].append(ult)
            q.append(ult)
        else:
            q.append(rep)
            q.append(lista[i])
        i += 1
    return ad

def main():
    global abc, ad
    cnt = int(stdin.readline())
    for k in range(1,cnt+1):
        lista = stdin.readline().strip()
        if(len(lista) != 2):
            res = solve(lista)
            print("Case", k)
            for i in range(26):
                if(len(res[i]) > 0):
                    print(abc[i],"=",len(res[i]))
        else:
            print("Case", k)
            print(lista[0],"= 0")
main()
    

    
