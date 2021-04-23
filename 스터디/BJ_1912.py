import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
sum = [0]*n
sum[0] = num[0]

for i in range(1, n):
    sum[i] = num[i]+sum[i-1]
bot = 0
gap = sum[0]
for i in range(1, n):
    bot = min(bot, sum[i-1])
    gap = max(gap, sum[i]-bot)

print(gap)