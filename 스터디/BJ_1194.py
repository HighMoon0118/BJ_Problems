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
            visit[r][c][0] = 1
        
que = deque()
que.append((0, sr, sc, 0))
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
alphaL = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5}
alphaU = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}
ans = -1
while que:
    dist, row, col, bit = que.popleft()
    print(row, col, dist)

    finish = 0
    for i in range(4):
        nr, nc = row+d[i][0], col+d[i][1]
        if 0<=nr<n and 0<=nc<m and board[nr][nc] != "#":

            if board[nr][nc] == "1":
                ans = dist + 1
                finish = 1
                break

            if board[nr][nc] != ".":
                c = board[nr][nc]
                if c in alphaL:
                    b = bit | (1 << alphaL[c])
                    if not visit[nr][nc][b]:
                        visit[nr][nc][b] = 1
                        que.append((dist+1, nr, nc, b))
                elif c in alphaU and bit & (1 << alphaU[c]) and not visit[nr][nc][bit]:
                    visit[nr][nc][bit] = 1
                    que.append((dist+1, nr, nc, bit))
            elif not visit[nr][nc][bit]:
                visit[nr][nc][bit] = 1
                que.append((dist+1, nr, nc, bit))
            
    if finish: break

print(ans)