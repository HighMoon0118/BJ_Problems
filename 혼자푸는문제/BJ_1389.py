import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
que = deque()
ans = []
for i in range(1, n+1) :
    order = [-1 for _ in range(n+1)]
    que.append(i)
    order[i] = 0
    while que :
        now = que.popleft()
        for next in graph[now] :
            if order[next]==-1 :
                order[next]=order[now]+1
                que.append(next)
    ans.append(sum(order))
a = min(enumerate(ans), key=lambda x : x[1])
print(a[0]+1)
