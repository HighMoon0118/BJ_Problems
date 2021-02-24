import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def intoQue(r, c):
    
    check[r][c]=True
    board[r][c]=num
    que.append((r, c, 0))

    if board[r+1][c]==1:
        intoQue(r+1,c)
    if board[r][c+1]==1:
        intoQue(r,c+1)
    if board[r-1][c]==1:
        intoQue(r-1,c)
    if board[r][c-1]==1:
        intoQue(r,c-1)



n = int(input())
board = [[0]*(n+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(n+2)]
ans = 1000
num = 1
for row in range(1, n+1):
    for col in range(1, n+1):
        if board[row][col]==1:
            num += 1
            check = [[True]*(n+2)]+[[True]+[False]*n+[True] for _ in range(n)]+[[True]*(n+2)]
            que = deque()
            intoQue(row, col)

            while que:
                nr, nc, d = que.popleft()
                if board[nr][nc]!=0 and board[nr][nc]!=num:
                    ans = min(ans, d)
                    break
                if not check[nr+1][nc]:
                    check[nr+1][nc] = True
                    que.append((nr+1,nc,d+1))
                if not check[nr][nc+1]:
                    check[nr][nc+1] = True
                    que.append((nr,nc+1,d+1))
                if not check[nr-1][nc]:
                    check[nr-1][nc] = True
                    que.append((nr-1,nc,d+1))
                if not check[nr][nc-1]:
                    check[nr][nc-1] = True
                    que.append((nr,nc-1,d+1))
print(ans-1)