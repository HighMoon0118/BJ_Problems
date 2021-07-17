import sys
sys.setrecursionlimit(1200000)

input = sys.stdin.readline

def makeIt(r, c, horse):

    if r==n-1 and c==m-1:
        return 0

    if dp[r][c][horse]: return dp[r][c][horse]

    dp[r][c][horse] = MAX
    
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and not board[nr][nc]:
            dp[r][c][horse] = min(dp[r][c][horse], 1 + makeIt(nr, nc, horse))

    if horse:
        for dr, dc in d2:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and not board[nr][nc]:
                dp[r][c][horse] = min(dp[r][c][horse], 1 + makeIt(nr, nc, horse-1))
    
    return dp[r][c][horse]


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d2 = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

k = int(input())
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

MAX = 400

ans = makeIt(0, 0, k)
    
if ans == MAX: print(-1)
else: print(ans)