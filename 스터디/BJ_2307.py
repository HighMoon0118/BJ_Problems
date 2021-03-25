import sys, heapq

input = sys.stdin.readline

def djt(s, e):
    time = [MAX_TIME for _ in range(n+1)]
    time[1] = 0
    heap = [(0, 1)]
    while heap:
        t, now = heapq.heappop(heap)
        if now==n: break
        for next, plus in graph[now]:
            if s==now and e==next or s==next and e==now: continue
            if t+plus < time[next]:
                time[next] = t+plus
                if not s: pre[next] = now
                heapq.heappush(heap, (time[next], next))
    return time[n]

MAX_TIME = 10000000
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

pre = [0 for _ in range(n+1)]

result = djt(0,0)

ans = -1
e = n
while pre[e]!=0:
    s = pre[e]
    tmp = djt(s, e)
    if tmp != MAX_TIME:
        tmp = tmp-result
        ans = max(ans, tmp)
    else:
        ans = -1
        break
    e = s
print(ans)