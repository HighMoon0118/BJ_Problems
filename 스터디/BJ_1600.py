import sys
from collections import deque

input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d2 = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

k = int(input())
m, n = map(int, input().split())
board = [[1]*(m+4) for _ in range(2)]+[[1, 1]+list(map(int, input().split()))+[1, 1] for _ in range(n)]+[[1]*(m+4) for _ in range(2)]

for r in range(n+4):
    for c in range(m+4):
        if board[r][c]: board[r][c] = 31
        else: board[r][c] = -1

que = deque()
que.append((2, 2, k, 0))
board[0][0] = k
isFinish = False

while que:
    r, c, h, cnt = que.popleft()
    if r==n+1 and c==m+1: 
        isFinish = True
        break
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if board[nr][nc] < h:
            board[nr][nc] = h
            que.append((nr, nc, h, cnt+1))
    
    if h:
        for dr, dc in d2:
            nr, nc = r+dr, c+dc
            if board[nr][nc] < h-1:
                board[nr][nc] = h-1
                que.append((nr, nc, h-1, cnt+1))

if isFinish: print(cnt)
else: print(-1)

# import sys
# sys.setrecursionlimit(1200000)

# input = sys.stdin.readline

# def makeIt(r, c, horse):

#     if r==n-1 and c==m-1:
#         return 0

#     if dp[r][c][horse]>=0: return dp[r][c][horse]

#     dp[r][c][horse] = MAX
    
#     for dr, dc in d:
#         nr, nc = r+dr, c+dc
#         if 0<=nr<n and 0<=nc<m and not board[nr][nc]:
#             dp[r][c][horse] = min(dp[r][c][horse], 1 + makeIt(nr, nc, horse))

#     if horse:
#         for dr, dc in d2:
#             nr, nc = r+dr, c+dc
#             if 0<=nr<n and 0<=nc<m and not board[nr][nc]:
#                 dp[r][c][horse] = min(dp[r][c][horse], 1 + makeIt(nr, nc, horse-1))
    
#     return dp[r][c][horse]


# d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# d2 = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


# k = int(input())
# m, n = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]


# dp = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]
# MAX = 400

# ans = makeIt(0, 0, k)
    
# if ans == MAX: print(-1)
# else: print(ans)