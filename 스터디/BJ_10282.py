import sys, heapq

tc = int(input())
ans = []
MAX_TIME = 10000000
for _ in range(tc):

    n, d, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    time = [MAX_TIME for _ in range(n+1)]

    for _ in range(d):
        a, b, t = map(int, input().split())
        graph[b].append((a,t))
    time[start] = 0
    que = [(0, start)]
    while que:
        t, now = heapq.heappop(que)
        if t > time[now] : continue
        for next, plus in graph[now]:
            if t+plus < time[next]:
                time[next] = t+plus
                heapq.heappush(que, (time[next], next))
    cnt = 0; last = 0
    for i in range(1, n+1):
        if time[i]<MAX_TIME: 
            cnt+=1
            if last < time[i]:
                last = time[i]
    ans.append("{} {}".format(cnt, last))
print("\n".join(ans))