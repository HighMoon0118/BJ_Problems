import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 200001
que = deque()
que.append((n, 0))
visit = [200000]*MAX
visit[n] = 0

ans = 0

while que:
    now, t = que.popleft()
    if now==k: continue
    if now < k:
        if now+1 < MAX and visit[now+1]>t+1:
            visit[now+1] = t+1
            que.append((now+1, t+1))
        if now*2 < MAX and visit[now*2] > t:
            visit[now*2] = t
            que.append((now*2, t))
    if 0 <= now-1 and visit[now-1] > t+1:
        visit[now-1] = t+1
        que.append((now-1, t+1))

print(visit[k])