import sys

input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

ans = 0

for i in range(n-1, 0, -1):
    if num[i]<=num[i-1]:
        score = num[i]-1
        ans += num[i-1]-score
        num[i-1] = score
print(ans)
