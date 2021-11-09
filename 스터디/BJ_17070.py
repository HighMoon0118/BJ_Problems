import sys

input = sys.stdin.readline

def dfs(row, col, how):
    if row==n-1 and col==n-1:
        return 1
    result = 0
    for pipe in next[how]:
        nr, nc = row+d[pipe][0], col+d[pipe][1]
        if 0<=nr<n and 0<=nc<n and not board[nr][nc]:
            if pipe!=2 or (not board[nr-1][nc] and not board[nr][nc-1]):
                result += dfs(nr, nc, pipe)
    return result

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

next = ((0, 2), (1, 2), (0, 1, 2))
d = ((0, 1), (1, 0), (1, 1))

print(dfs(0, 1, 0))