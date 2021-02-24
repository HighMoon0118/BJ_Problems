import sys

input = sys.stdin.readline

def dfs(r, c):
    visited[r][c] = True
    result = 0
    if not visited[r+1][c] and board[r+1][c] : result += 1+dfs(r+1, c)
    if not visited[r][c+1] and board[r][c+1] : result += 1+dfs(r, c+1)
    if not visited[r-1][c] and board[r-1][c] : result += 1+dfs(r-1, c)
    if not visited[r][c-1] and board[r][c-1] : result += 1+dfs(r, c-1)
    return result

n = int(input())
board = [[0]*(n+2)] + [[0]+list(map(int, input().strip()))+[0] for _ in range(n)] + [[0]*(n+2)]
visited = [[False for _ in range(n+2)] for _ in range(n+2)]
ans = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if not visited[i][j] and board[i][j]:
            ans.append(1+dfs(i,j))
ans.sort()
print(len(ans))
print("\n".join(map(str, ans)))