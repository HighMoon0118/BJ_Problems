import sys
sys.setrecursionlimit(50000)

input = sys.stdin.readline

def dfs(idx, d, total):

    visit[idx] = 1
    depth[idx] = d
    distance[idx] = total

    for node, dist in tree[idx]:
        if not visit[node]:
            parent[node] = idx
            dfs(node, d+1, total+dist)

n = int(input())
tree = [list() for _ in range(n+1)]

for _ in range(n-1):
    a, b, dist = map(int, input().split())
    tree[a].append((b, dist))
    tree[b].append((a, dist))

depth = [0]*(n+1)
visit = [0]*(n+1)
parent = [0]*(n+1)
distance = [0]*(n+1)

dfs(1, 0, 0)

m = int(input())
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    if depth[a] < depth[b]: a, b = b, a
    gap = depth[a] - depth[b]
    ans = distance[a]+distance[b]
    while gap:
        a = parent[a]
        gap -= 1

    while a != b:
        a, b = parent[a], parent[b]
    ans -= distance[a]*2
    answer.append(ans)

print("\n".join(map(str, answer)))

