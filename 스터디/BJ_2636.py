import sys
sys.setrecursionlimit(10000)
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
d = [(0,1), (1,0), (0,-1), (-1,0)]

def fillOut(row, col):
    board[row][col] = -1
    for dr, dc in d:
        nr, nc = row+dr, col+dc
        if 0<=nr<n and 0<=nc<m and board[nr][nc]==0:
            fillOut(nr, nc)

time = cnt = 0
que = deque()
que.append((0, 0))

while True:
    while que:
        r, c = que.popleft()
        fillOut(r, c)
    for r in range(1, n-1):
        for c in range(1, m-1):
            if board[r][c]==1 and (board[r][c+1]==-1 or board[r+1][c]==-1 or board[r][c-1]==-1 or board[r-1][c]==-1):
                board[r][c] = 0
                que.append((r, c))
    ans = cnt
    cnt = len(que)
    if not cnt: break
    time += 1

print(time, ans)