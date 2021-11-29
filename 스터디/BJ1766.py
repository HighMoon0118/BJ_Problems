import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())

tree = [list() for _ in range(n+1)]
child = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    child[b] += 1

que = []
for i in range(1, n+1):
    if child[i] == 0: que.append(i)

solved = [0]*(n+1)
ans = []

while que:
    now = heappop(que)
    if solved[now]: continue
    solved[now] = True
    ans.append(now)

    for node in tree[now]:
        child[node] -= 1
        if child[node] == 0:
            heappush(que, node)

print(" ".join(map(str, ans)))