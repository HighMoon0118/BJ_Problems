import sys

input = sys.stdin.readline

def make_it(index):
    if index==n: return 0

    if dp[index]: return dp[index]

    i = index+1
    dp[index] = num[index]
    while i<n:
        if num[index] < num[i]:
            dp[index] = max(dp[index], num[index] + make_it(i))
        i += 1
    return dp[index]

n = int(input())
num = list(map(int, input().split()))
dp = [0]*(n)
for i in range(n):
    make_it(i)
print(max(dp))