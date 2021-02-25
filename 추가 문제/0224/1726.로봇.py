import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

board = [[1]*(m+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(n)]+[[1]*(m+2)]

sr, sc, sway = map(int, input().split())
er, ec, eway = map(int, input().split())
sway-=1; eway-=1
if sway==1: sway=2
elif sway==2: sway=1
if eway==1: eway=2
elif eway==2: eway=1


dist = [[[0 for _ in range(4)] for _ in range(m+2)] for _ in range(n+2)]
dist[sr][sc][sway] = 1
que = deque()
que.append((sr,sc,sway))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while que:
    r, c, way = que.popleft()
    if r==er and c==ec:
        if way==eway:
            break
        left, right = (way+3)%4, (way+1)%4
        if not dist[r][c][left]:
            dist[r][c][left] = dist[r][c][way]+1
            que.append((r, c, left))
        if not dist[r][c][right]:
            dist[r][c][right] = dist[r][c][way]+1
            que.append((r, c, right)) 
        continue

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if not board[nr][nc]:
            if way!=i:
                left, right = (way+3)%4, (way+1)%4
                if not dist[r][c][left]:
                    dist[r][c][left] = dist[r][c][way]+1
                    que.append((r, c, left))
                if not dist[r][c][right]:
                    dist[r][c][right] = dist[r][c][way]+1
                    que.append((r, c, right))
            else:
                count = 0
                while not board[nr][nc]:
                    count += 1
                    if not dist[nr][nc][way]:
                        dist[nr][nc][way] = dist[r][c][way]+1
                        que.append((nr, nc, way))
                    nr, nc = nr+dr[i], nc+dc[i]
                    if count == 3:
                        break
    
print(dist[er][ec][eway]-1)