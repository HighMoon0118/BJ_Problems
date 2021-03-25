import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [200000 for _ in range(n+1)]
dist[start] = 0
heap = [(0, start)]
while heap:
    d, now = heapq.heappop(heap)
    for next, w in graph[now]:
        if d+w < dist[next]:
            dist[next] = d+w
            heapq.heappush(heap, (dist[next], next))

ans = []
for i in range(1, n+1):
    if dist[i]==200000:
        ans.append("INF")
    else:
        ans.append(str(dist[i]))
print("\n".join(ans))