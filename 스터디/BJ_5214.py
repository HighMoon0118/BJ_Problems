import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

hypers = []
que = deque()
link = [set() for _ in range(m)]
visited = [0]*(m)
end = set()

for i in range(m):
    hypers.append(set(map(int, input().split())))
    if 1 in hypers[i]:
        que.append((i, 1))
        visited[i] = 1
    if n in hypers[i]:
        end.add(i)

for i in range(m):
    for station in hypers[i]:
        for j in range(i+1, m):
            if station in hypers[j]:
                link[i].add(j)
                link[j].add(i)

while que:
    s, dist = que.popleft()
    if s in end: break
    for hyper in link[s]:
        if not visited[hyper]:
            visited[hyper] = 1
            que.append((hyper, dist+1))
                
if s in end: print(dist+1)
else: print(-1)