from sys import stdin

def solve(num, n):
    i, acum, ans = 1, 0, 0
    while(i < n):
        acum = num[i] - num[i-1]
        if(acum > ans):
            ans = acum
        i += 1
    return ans

def main():
    tcnt = int(stdin.readline())
    for tc in range(1, tcnt+1):
        n = int(stdin.readline())
        num = [ int(x) for x in stdin.readline().split() ]
        print('Case {0}: {1}'.format(tc, solve(num, n)))

main()
