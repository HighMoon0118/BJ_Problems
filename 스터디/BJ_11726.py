import sys
sys.setrecursionlimit(2000)

def make_it(i):
    if i==n: return 1
    elif i>n: return 0

    if dp[i]: return dp[i]

    dp[i] = make_it(i+1) + make_it(i+2)
    return dp[i]

n = int(input())
dp = [0]*(n+1)
print(make_it(0)%10007)