import sys
from collections import deque

n = int(input())

board = []

for i in range(n) :
    board.append(list(input().strip()))

visited = [[0 for _ in range(n)] for _ in range(n)]

que = deque()

dr = 0, 1, 0, -1
dc = 1, 0, -1, 0

ans1, ans2 = 0, 0

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            ans1+=1
            visited[i][j]=1
            que.append((i, j, board[i][j]))
            while que :
                r, c, color = que.popleft()
                if color == 'G' : board[r][c]='R'
                
                for k in range(4) :
                    nr, nc = r+dr[k], c+dc[k]
                    if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and board[nr][nc]==color :
                        visited[nr][nc]=1
                        que.append((nr, nc, color))

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            ans2+=1
            visited[i][j]=1
            que.append((i, j, board[i][j]))
            while que :
                r, c, color = que.popleft()
                for k in range(4) :
                    nr, nc = r+dr[k], c+dc[k]
                    if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and board[nr][nc]==color :
                        visited[nr][nc]=1
                        que.append((nr, nc, color))
                
print(ans1, ans2)