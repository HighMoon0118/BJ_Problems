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
        c, path = heapq.heappop(que)  # c는 시작지점으로부터 번 돈, path는 시작지점으롤부터 경로
        now = path[-1]  # 마지막에 방문한 노드
        if cycle[now]: continue  # 만약 현재 노드가 cycle과 연결된 노드라면 방문할 필요 없음(dfs로 다 돌아봤기 때문)
        for next, plus in graph[now]:
            if cost[next] > c + plus - money[next]:
                cost[next] = c + plus - money[next]
                if next in path:  # 최단거리가 업데이트 됐 지점이 이전에 방문했던 곳이면 사이클이라고 판별
                    dfs(next)  # 그 지점으로부터 연결된 노드들은 다 무한으로 돈을 벌 수 있는 지점
                    if cycle[end]: return "Gee"  # 끝 지점도 무한으로 돈을 벌 수 있다면 Gee
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

cycle = [False for _ in range(n)]  # 사이클과 연결된 노드인지 판별

print(djt())