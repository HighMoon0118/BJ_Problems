import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    s, e, c = map(int, input().split())
    if c < graph[s][e]:
        graph[s][e] = c

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if graph[s][e] > graph[s][k] + graph[k][e]:
                graph[s][e] = graph[s][k] + graph[k][e]

ans = []
for i in range(1, n+1):
    tmp = ""
    for j in range(1, n+1):
        if graph[i][j] != sys.maxsize:
            tmp += f"{graph[i][j]} "
        else:
            tmp += "0 "
    ans.append(tmp)
print("\n".join(ans))