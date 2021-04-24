import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
MAX = max(num)
dp = [0]*(MAX+2)

for i in num:
    dp[i] = max(dp[i+1:])+1

print(max(dp))
print(dp)