import sys

input = sys.stdin.readline

def dfs(how, row, col):
    global ans

    if row==n and col==n:
        return 1

    if dp[how][row][col] >= 0: return dp[how][row][col]

    result = 0
    for pipe in next[how]:
        nr, nc = row+d[pipe][0], col+d[pipe][1]
        if not board[nr][nc] and (pipe!=2 or not (board[nr-1][nc] or board[nr][nc-1])):
            result += dfs(pipe, nr, nc)
    dp[how][row][col] = result

    return dp[how][row][col]      

n = int(input())
board = [[1]*(n+2)] + [[1]+list(map(int, input().split()))+[1] for _ in range(n)] + [[1]*(n+2)]

next = ((0, 2), (1, 2), (0, 1, 2))
d = ((0, 1), (1, 0), (1, 1))

dp = [[[-1]*(n+2) for _ in range(n+2)] for _ in range(3)]

print(dfs(0, 1, 2))