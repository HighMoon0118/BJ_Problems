import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def make_it(r, c):
    if n<=r or n<=c:
        return 0
    
    if r==n-1 and c==n-1:
        return 1
    
    if dp[r][c]>=0: return dp[r][c]

    dp[r][c] = 0
    dp[r][c] = make_it(r+board[r][c], c) + make_it(r, c+board[r][c])
    return dp[r][c]

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]  # 0이면 메모리 초과 or recrusion
print(make_it(0, 0))