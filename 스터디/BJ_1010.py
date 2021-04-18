import sys

input = sys.stdin.readline

def make_it(a, b):  # nCr = n-1Cr + n-1Cr-1
    if b==0 or a==b: return 1
    if dp[a][b] >=0: return dp[a][b]
    
    dp[a][b] = make_it(a-1, b) + make_it(a-1, b-1)
    return dp[a][b]

t = int(input())
    
dp = [[-1 for _ in range(31)] for _ in range(31)]
ans = []
for tc in range(1, t+1):
    n, m = map(int, input().split())

    ans.append(str(make_it(m, n)))
print("\n".join(ans))