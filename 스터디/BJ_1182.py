import sys

input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
ans = 0

MAX = 1<<n
ans = 0
for i in range(1, MAX):
    tmp = 0
    for j in range(n):
        if i&(1<<j):
            tmp += num[j]
    if tmp==s:
        ans +=1
print(ans)