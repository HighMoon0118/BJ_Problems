import sys
from heapq import heappush, heappop

def heap(start):
    
    dist = [MAX for _ in range(n+1)]
    que = [(0, start)]
    dist[start] = 0
    while que:
        cost, now = heappop(que)
        for b, c in graph[now]:
            if dist[b] > cost + c:
                dist[b] = cost + c
                heappush(que, (dist[b], b))
    return dist

input = sys.stdin.readline

MAX = 200000000
n, e = map(int, input().split())
graph = [list() for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

fromV1 = heap(v1)
fromV2 = heap(v2)

dist1 = fromV1[1]+fromV1[v2]+fromV2[n]
dist2 = fromV2[1]+fromV2[v1]+fromV1[n]

ans = min(dist1, dist2)
if ans >= MAX: print(-1)
else: print(ans)