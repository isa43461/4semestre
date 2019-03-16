from sys import stdin

def solve(ladies, x):
    l, h = 0 ,len(ladies)
    while(l+1 != h and ladies[l] != x):
        mid = l + ((h-l)>>1) 
        if(x < ladies[mid]): h = mid
        else: l = mid
    lt, rt = "X", "X"
    if (ladies[l] == x and l-1 >= 0):
        lt =  str(ladies[l-1])
    elif (ladies[l] != x and ladies[l] < x):
        lt = str(ladies[l])
    if (ladies[l]== x and l+1 < len(ladies)):
        rt = ladies[l+1]
    elif (ladies[l] != x and ladies[l] > x):
        rt = ladies[l]
    elif(ladies[l] != x and l+1 < len(ladies)):
        rt = ladies[l+1]
    print('{} {}'.format(lt,rt))
    
def main():
  inp = stdin
  inp.readline()
  ladies = sorted(list(set([int(x) for x in inp.readline().split()])))
  inp.readline()
  queries = (list([int(x) for x in inp.readline().split()]))
  for x in queries:
    solve(ladies, x)
  
main()
