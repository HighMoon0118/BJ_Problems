import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().strip()) for _ in range(n)]
visit = [[[0]*(1<<6) for _ in range(m)] for _ in range(n)]

for r in range(n):
    for c in range(m):
        if board[r][c] == "0":
            sr, sc = r, c
            board[r][c] = "."
        
que = deque()
que.append((0, sr, sc, 0))
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
alphaL = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5}
alphaU = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}
ans = -1
while que:
    dist, row, col, bit = que.popleft()
    
    if visit[row][col][bit]: continue
    visit[row][col][bit] = 1
    if board[row][col] == "1":
        ans = dist
        break

    for i in range(4):
        nr, nc = row+d[i][0], col+d[i][1]
        if 0<=nr<n and 0<=nc<m and board[nr][nc] != "#":
            if board[nr][nc] == "." or board[nr][nc] == "1": que.append((dist+1, nr, nc, bit))
            else:
                c = board[nr][nc]
                if c in alphaL: que.append((dist+1, nr, nc, bit|(1<<alphaL[c])))
                elif c in alphaU and bit & (1 << alphaU[c]): que.append((dist+1, nr, nc, bit))
print(ans)