import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())
board = [[9]*(w+2)] + [[] for _ in range(h)] + [[9]*(w+2)]
visited = [[False for _ in range(w+2)] for _ in range(h+2)]
water = deque()
for i in range(1,h+1):
    board[i].append(9)
    for j, c in enumerate(input().strip()):
        if c==".": 
            board[i].append(0)
            visited[i][j+1] = True
            water.append((i,j+1,0))
        else: board[i].append(int(c))
    board[i].append(9)
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]
while water:
    r, c, d = water.popleft()
    for i in range(8):
        board[r+dr[i]][c+dc[i]] -= 1
    for i in range(8):
        nr, nc = r+dr[i], c+dc[i]
        if not visited[nr][nc] and board[nr][nc]<=0:
            visited[nr][nc] = True
            water.append((nr, nc, d+1))
print(d)