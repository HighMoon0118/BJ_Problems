import sys

input = sys.stdin.readline

d = [(0,1), (1,0), (0,-1), (-1,0)]

def makeIt(row, col):

    if row==n and col==m: return 1

    if dp[row][col] >= 0: return dp[row][col]
    
    cnt = 0
    for i in range(4):
        nr, nc = row+d[i][0], col+d[i][1]
        if board[row][col] > board[nr][nc]:
            cnt += makeIt(nr, nc)

    dp[row][col] = cnt
    return dp[row][col]
    

n, m = map(int, input().split())

board = [[10001]*(m+2)] + [[10001]+list(map(int, input().split()))+[10001] for _ in range(n)] + [[10001]*(m+2)]
dp = [[-1]*(m+2) for _ in range(n+2)]
print(makeIt(1, 1))
