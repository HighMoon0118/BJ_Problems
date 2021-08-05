import sys, heapq

sys.setrecursionlimit(100000000)

input = sys.stdin.readline

n, m = map(int, input().split())

bridge = [dict() for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in bridge[a]:
        if bridge[a][b] < c:
            bridge[a][b] = c
            bridge[b][a] = c
    else:
        bridge[a][b] = c
        bridge[b][a] = c

start, end = map(int, input().split())
visit = [0]*(n+1)

que = []

heapq.heappush(que, (-1000000000, start))

while que:

    cost, idx = heapq.heappop(que)
    
    if visit[idx]: continue
    visit[idx] = 1
    
    if idx==end:
        break

    for i, c in bridge[idx].items():
        heapq.heappush(que, (max(cost, -c), i))

print(-cost)