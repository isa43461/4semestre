from sys import stdin
MAX = 10010
bet = [None for i in range(10010)]

def max_crossing(A, low, mid, hi):
  bestl,accl,l = A[mid-1],A[mid-1],mid-2
  while (l >= low):
    accl += A[l]
    if (accl > bestl): bestl = accl
    l -= 1
  bestr,accr,r = A[mid],A[mid],mid+1
  while (r != hi):
    accr += A[r]
    if (accr > bestr): bestr = accr
    r += 1
  return bestl + bestr
  
def mss(A, low, hi):
  ans = 0
  if (low + 1 == hi):
    ans = A[low]
  else:
    mid = low + ((hi-low)>>1) 
    ans = max(mss(A, low, mid), mss(A, mid, hi))
    ans = max(ans, max_crossing(A, low, mid, hi))
  return ans

def solve(A, n):
  return max(0, mss(A, 0, n))

def main():
  global bet
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): bet[i] = int(tok[i])
    x = solve(bet, n)
    if x <=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(x))
    n = int(inp.readline().strip())

main()
