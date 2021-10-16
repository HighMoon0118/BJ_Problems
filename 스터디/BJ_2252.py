import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

parentOf = [list() for _ in range(n+1)]
childs = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    parentOf[b].append(a)
    childs[a] += 1

leaf = deque()
for i in range(1, n+1):
    if not childs[i]:
        leaf.append(i)

ans = []
while leaf:
    now = leaf.popleft()
    for p in parentOf[now]:
        childs[p] -= 1
        if not childs[p]:
            leaf.append(p)
    ans.append(str(now))

print(" ".join(ans[::-1]))