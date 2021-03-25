import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
MAX = sys.maxsize
graph = [[] for _ in range(n+1)]
time = [MAX for _ in range(n+1)]
pre = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

time[1] = 0
que = [(0, 1)]
while que:
    t, now = heapq.heappop(que)
    if t > time[now]: continue
    for next, plus in graph[now]:
        if t+plus < time[next]:
            time[next] = t+plus
            pre[next] = now
            heapq.heappush(que, (time[next], next))
ans = []
cnt = 0
checked = [False for _ in range(n+1)]
for i in range(1, n+1):
    if pre[i] and not checked[i]:
        cnt += 1
        ans.append(f"{i} {pre[i]}")
        checked[i] = True
print(cnt)
print("\n".join(ans))