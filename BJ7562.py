import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for i in range(n) :
    board.append(list(map(int, input().strip())))
    
visited = [[0 for _ in range(m)] for _ in range(n)]

dr = 0, 1, 0, -1
dc = 1, 0, -1, 0

que = deque()
que.append((0,0,1,1))
visited[0][0]=1
finish = False

while que :
    r, c, boom, count = que.popleft()
    if r==n-1 and c==m-1 : 
        finish=True
        break
    for i in range(4) :
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m :
            if board[nr][nc]==0 :
                if not visited[nr][nc] or visited[nr][nc]>boom :
                    visited[nr][nc]=boom
                    que.append((nr, nc, boom, count+1))
            elif boom==1 :
                visited[nr][nc]=boom+1
                que.append((nr, nc, boom+1, count+1))

if finish : print(count)
else : print(-1)