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
  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0:
    n = int(s)
    num = [int(x) for x in inp.readline().strip().split()]
    print(lab.format(solve(num)))
    s = inp.readline().strip()

main()
