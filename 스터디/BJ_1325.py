import sys
sys.setrecursionlimit(10001)

input = sys.stdin.readline
def dfs(i):
    visited[i] = True
    for next in board[i]:
        if not visited[next]:
            child[next]+=1
            dfs(next)

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)

child = [0 for _ in range(n+1)]
ans = []
tmp = 0
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)

for i in range(1, n+1):
    tmp = max(tmp, child[i])

for i in range(1, n+1):
    if child[i] == tmp:
        ans.append(i)

print(*ans)