import sys
sys.setrecursionlimit(20000)

input = sys.stdin.readline

def dfs(node, dist):
    global start, maxD

    if dist>maxD:
        maxD = dist
        start = node

    visited[node] = True

    for child, plus in tree[node]:
        if not visited[child]:
            dfs(child, dist+plus)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited = [0]*(n+1)
start = maxD = 0
dfs(1, 0)
visited = [0]*(n+1)
dfs(start, 0)
print(maxD)