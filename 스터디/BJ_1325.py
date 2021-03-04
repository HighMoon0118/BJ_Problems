import sys
sys.setrecursionlimit(10001)

input = sys.stdin.readline
def dfs(i):
    visited[i] = True
    used[i] = True

    result = 1
    for next in board[i]:
        if not visited[next]:
            result += dfs(next)
    return result

n, m = map(int, input().split())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[b].append(a)

child = [0 for _ in range(n+1)]
used = [False for _ in range(n+1)]
ans = []
tmp = 0
for i in range(1, n+1):
    if not used[i]:
        visited = [False for _ in range(n+1)]
        child[i] = dfs(i)
        tmp = max(tmp, child[i])

for i in range(1, n+1):
    if child[i] == tmp:
        ans.append(i)

print(*ans)