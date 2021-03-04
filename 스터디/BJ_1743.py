import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(row, col):
    board[row][col] = 0
    result = 1
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if board[nr][nc]:
            result += dfs(nr, nc)
    return result

n, m, k = map(int, input().split())
board = [[0 for _ in range(m+2)] for _ in range(n+2)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j]:
            ans = max(ans, dfs(i,j))
print(ans)