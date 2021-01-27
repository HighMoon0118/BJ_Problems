import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

board = [[] for _ in range(h)]
que = deque()

for i in range(h) :
    for j in range(n) :
        board[i].append(list(map(int, input().split())))
        for k in range(m) :
            if board[i][j][k]==1 :
                que.append((i,j,k,0))

def finished() :
    for i in range(h) :
        for j in range(n) :
            for k in range(m) :
                if board[i][j][k]==0 :
                    return False
    return True

while que :
    z, y, x, count = que.popleft()

    if y>0 and board[z][y-1][x]==0 :
        board[z][y-1][x]=1
        que.append((z, y-1, x, count+1))
    if y<n-1 and board[z][y+1][x]==0 :
        board[z][y+1][x]=1
        que.append((z, y+1, x, count+1))
    if x>0 and board[z][y][x-1]==0 :
        board[z][y][x-1]=1
        que.append((z, y, x-1, count+1))
    if x<m-1 and board[z][y][x+1]==0 :
        board[z][y][x+1]=1
        que.append((z, y, x+1, count+1))
    if z>0 and board[z-1][y][x]==0 :
        board[z-1][y][x]=1
        que.append((z-1, y, x, count+1))
    if z<h-1 and board[z+1][y][x]==0 :
        board[z+1][y][x]=1
        que.append((z+1, y, x, count+1))

if finished() : 
    print(count)
else :
    print(-1)