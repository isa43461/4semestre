from sys import stdin
def solve(num):
    r = 0
    if(len(num) > 1):
        mid = len(num)>>1
        izq = num[:mid]
        der = num[mid:]
        r += solve(izq)
        r += solve(der)
        f,i,j = 0,0,0
        while(i < len(izq) or j < len(der)):
            if(i < len(izq) and j < len(der)):
                if(izq[i] <= der[j]):
                    num[f] = izq[i]
                    i += 1
                    f += 1
                else:
                    num[f] = der[j]
                    j += 1
                    f += 1
                    r += (len(izq)-i) 
            elif(i < len(izq)):
                num[f] = izq[i]
                i += 1
                f += 1
            elif(j < len(der)):
                num[f] = der[j]
                j += 1
                f += 1
    return r

def main():
    cases = int(stdin.readline())
    while cases != 0:
        num = int(stdin.readline())
        l = stdin.readline().strip().split()
        lista = [int(i) for i in l]
        print("Optimal train swapping takes",solve(lista),"swaps.")
        cases -= 1
main()