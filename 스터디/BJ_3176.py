import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(idx, d):

    visit[idx] = 1
    depth[idx] = d

    for node, dist in tree[idx]:
        if not visit[node]:
            parent[node] = (idx, dist)
            dfs(node, d+1)

n = int(input())
tree = [list() for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

visit = [0]*(n+1)
depth = [0]*(n+1)
parent = [tuple() for _ in range(n+1)]
dfs(1, 0)

minMax = [dict() for i in range(n+1)]
for i in range(n, -1, -1):
    node = i
    MIN, MAX = 1000000, 0
    while parent[node]:
        node, dist = parent[node]
        MIN, MAX = min(MIN, dist), max(MAX, dist)
        minMax[i][node] = (MIN, MAX)

k = int(input())
answer = []
for _ in range(k):
    a, b, = map(int, input().split())
    sA, sB = a, b
    if depth[a] < depth[b]: a, b = b, a
    gap = depth[a]-depth[b]
    while gap:
        a = parent[a][0]
        gap -= 1

    while a!=b:
        a = parent[a][0]
        b = parent[b][0]

    minA, maxA = minMax[sA][a] if sA!=a else (1000000, 0)
    minB, maxB = minMax[sB][b] if sB!=b else (1000000, 0)
    MIN, MAX = min(minA, minB), max(maxA, maxB)
    answer.append(str(MIN)+" "+str(MAX))

print("\n".join(answer))