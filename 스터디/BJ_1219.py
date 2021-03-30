import sys, heapq

input = sys.stdin.readline

def dfs(s):
    cycle[s] = True
    for next, plus in graph[s]:
        if not cycle[next]:
            dfs(next)

def djt():
    que = [(cost[start], [start])]
    while que:
        c, path = heapq.heappop(que)
        now = path[-1]
        if cycle[now]: continue
        for next, plus in graph[now]:
            if cost[next] > c + plus - money[next]:
                cost[next] = c + plus - money[next]
                if next in path:
                    dfs(next)
                    if cycle[end]: return "Gee"
                else:
                    heapq.heappush(que, (cost[next], path+[next]))
    if cost[end]==MAX: return "gg"
    return -cost[end]

n, start, end, m = map(int, input().split())
MAX = sys.maxsize

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

money = tuple(map(int, input().split()))

cost = [MAX for _ in range(n)]
cost[start] = -money[start]

cycle = [False for _ in range(n)]

print(djt())