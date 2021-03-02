import sys
from collections import deque

m, n = map(int, input().split())
board = []
que = deque()

for i in range(n) :
    board.append(list(map(int, sys.stdin.readline().split())))
    board[i].append(-1)
    for j in range(m) :
        if board[i][j]==1 :
            que.append((i, j, 0))

board.append([-1 for _ in range(m+1)])

def isFinished() :
    for i in range(n) :
        for j in range(m) :
            if board[i][j]==0 :
                return False
    return True

ans = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while que :
    
    r,c,count = que.popleft()
    
    for i in range(4) :
        nextR, nextC = r+dr[i], c+dc[i]
        if 0<=nextR and 0<=nextC and board[nextR][nextC]==0 :
            board[nextR][nextC]=1
            ans = count+1
            que.append((nextR, nextC, ans))


if isFinished() : print(ans)
else : print(-1)
    
