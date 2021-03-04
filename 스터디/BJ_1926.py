import sys
sys.setrecursionlimit(250000)
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

n, m = map(int, input().split())
board = [[0]*(m+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
total = maxW = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j]:
            total += 1
            maxW = max(maxW, dfs(i,j))
print(total)
print(maxW)