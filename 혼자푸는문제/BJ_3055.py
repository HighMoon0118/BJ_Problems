import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
water = []
for i in range(n) :
    board.append(list(input().strip()))
    for j in range(m) :
        if board[i][j]=='S' :
            gd = i, j
            board[i][j]='.'
        elif board[i][j]=='*' :
            water.append((i,j))
            board[i][j]='.'

dr = 0, 1, 0, -1
dc = 1, 0, -1, 0

que = deque()
waterTime = [[100 for _ in range(m)] for _ in range(n)]

if len(water)>0 : 
    for w in water :
        que.append(w)
        waterTime[w[0]][w[1]]=0

while que :
    r, c = que.popleft()
    for i in range(4) :
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and waterTime[nr][nc]==100 and board[nr][nc]!='X' and board[nr][nc]!='D' :
            waterTime[nr][nc] = waterTime[r][c]+1
            que.append((nr, nc))

gdTime = [[-1 for _ in range(m)] for _ in range(n)]
gdTime[gd[0]][gd[1]]=0
que.append(gd)

finish = False

while que :
    r, c = que.popleft()
    if board[r][c]=='D' : 
        finish = True
        break
    for i in range(4) :
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and gdTime[nr][nc]==-1 and board[nr][nc]!='X':
            if gdTime[r][c] < waterTime[r][c] :
                gdTime[nr][nc]=gdTime[r][c]+1
                que.append((nr, nc))

if finish : print(gdTime[r][c])
else : print('KAKTUS')