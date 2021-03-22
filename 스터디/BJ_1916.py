import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    bus[a].append((d, b))
start, end = map(int, input().split())
dist = [100000000 for _ in range(n+1)]
dist[start] = 0 
heap = [(dist[start], start)]
while heap:
    d, now = heapq.heappop(heap)
    if now==end:
        break
    for plus, next in bus[now]:
        if d + plus < dist[next]:
            dist[next] = d+ plus
            heapq.heappush(heap, (dist[next], next))
print(dist[end])