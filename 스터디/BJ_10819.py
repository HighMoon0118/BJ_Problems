import sys

input = sys.stdin.readline


n = int(input())

num = list(map(int, input().split()))
used = [0]*n
ans = 0
def makeIt(pre, cnt, total):
    global ans

    if cnt == n:
        ans = max(ans, total)
        return

    for i in range(n):
        if not used[i]:
            used[i] = 1
            makeIt(i, cnt+1, total + abs(num[pre]-num[i]))
            used[i] = 0


for i in range(n):
    used[i] = 1
    makeIt(i, 1, 0)
    used[i] = 0

print(ans)