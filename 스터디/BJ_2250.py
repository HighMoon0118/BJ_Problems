import sys

input = sys.stdin.readline

n = int(input())
tree = [[-1, -1] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n):
    i, a, b = map(int, input().split())
    tree[i][0] = a
    tree[i][1] = b
    if a>0: parent[a] = i
    if b>0: parent[b] = i

visit = [0]*(n+1)
x = [list() for _ in range(n+1)]
num = 0

root = 1
while parent[root]>0: root = parent[root]

def dfs(idx, d):
    global num

    if tree[idx][0]>0: dfs(tree[idx][0], d+1)
    x[d].append(num)
    num += 1
    if tree[idx][1]>0: dfs(tree[idx][1], d+1)

dfs(root, 0)

maxW = 0
idx = 0
for i in range(n+1):
    if not x[i]: break
    w = x[i][-1]-x[i][0]+1
    if maxW < w:
        idx = i+1; maxW = w

print(idx, maxW)