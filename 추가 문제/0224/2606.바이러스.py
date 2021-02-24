import sys

input = sys.stdin.readline
def dfs(i):
    visited[i] = True
    result = 0
    for j in graph[i]:
        if not visited[j]:
            result += 1+dfs(j)
    return result
n = int(input())
l = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(1))
