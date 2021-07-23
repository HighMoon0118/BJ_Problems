import sys

input = sys.stdin.readline

n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]
used = [0]*n
ans = 10000000

def makeIt(pre, cnt, total, start):
    global ans

    if cnt==n:
        if cost[pre][start]:
            ans = min(ans, total+cost[pre][start])
        return

    for i in range(n):
        if not used[i] and cost[pre][i]:
            used[i] = 1
            makeIt(i, cnt+1, total+cost[pre][i], start)
            used[i] = 0

for i in range(n):
    used[i] = 1
    makeIt(i, 1, 0, i)
    used[i] = 0
    
print(ans)