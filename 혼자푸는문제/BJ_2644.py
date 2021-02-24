import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()
que.append(start)
visited = [ 0 for _ in range(n+1)]
visited[start]=1

while que :
    now = que.popleft()
    if now == end : break
    for next in graph[now] :
        if not visited[next] :
            visited[next]=visited[now]+1
            que.append(next)

print(visited[end]-1)