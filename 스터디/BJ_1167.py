import sys

input = sys.stdin.readline

def dfs(node, dist):
    global start, maxD

    if dist > maxD:
        maxD = dist
        start = node

    visited[node] = True

    for child, plus in link[node]:
        if not visited[child]:
            dfs(child, dist+plus)

v = int(input())

link = [[] for _ in range(v+1)]
for _ in range(v):
    a, *tmp, end = map(int, input().split())
    for i in range(0, len(tmp), 2):
        link[a].append((tmp[i], tmp[i+1]))

visited = [0]*(v+1)
start = maxD = 0
dfs(1, 0)
maxD = 0
visited = [0]*(v+1)
dfs(start, 0)
print(maxD)