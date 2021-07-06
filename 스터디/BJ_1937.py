import sys
sys.setrecursionlimit(250000)

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def makeIt(r, c):

    if dp[r][c]>=0: dp[r][c]

    result = 0
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if board[nr][nc] and board[r][c] < board[nr][nc]:
            result = max(result, 1 + makeIt(nr, nc))
    dp[r][c] = result
    return dp[r][c]


n = int(input())

board = [[0]*(n+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(n)] + [[0]*(n+2)]

dp = [[-1]*(n+2) for _ in range(n+2)]
ans = 0
for r in range(1, n+1):
    for c in range(1, n+1):
        ans = max(ans, makeIt(r, c))
print(ans+1)