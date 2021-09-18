import sys
sys.setrecursionlimit(60000)

input = sys.stdin.readline

def dfs(idx, d):
    depth[idx] = d
    visit[idx] = 1

    for node in tree[idx]:
        if not visit[node]:
            dfs(node, d+1)
            parent[node] = idx


n = int(input())

tree = [list() for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [0]*(n+1)
depth = [0]*(n+1)
parent = [0]*(n+1)

dfs(1, 0)

m = int(input())
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        gap = depth[a] - depth[b]
        while gap:
            a = parent[a]
            gap -= 1
    elif depth[a] < depth[b]:
        gap = depth[b] - depth[a]
        while gap:
            b = parent[b]
            gap -= 1
    
    while a != b:
        a = parent[a]
        b = parent[b]
    ans.append(str(a))

print("\n".join(ans))