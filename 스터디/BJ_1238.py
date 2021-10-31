import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph1 = [list() for _ in range(n+1)]
graph2 = [list() for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph1[b].append((a, t))
    graph2[a].append((b, t))

take1 = [100001]*(n+1)
que = [(0, x)]
while que:
    time, now = heappop(que)
    if take1[now] <= time: continue
    take1[now] = time
    for city, t in graph1[now]:
        heappush(que, (time+t, city))

take2 = [100001]*(n+1)
que = [(0, x)]
while que:
    time, now = heappop(que)
    if take2[now] <= time: continue
    take2[now] = time
    for city, t in graph2[now]:
        heappush(que, (time+t, city))
ans = 0
for i in range(1, n+1):
    ans = max(ans, take1[i]+take2[i])
print(ans)    