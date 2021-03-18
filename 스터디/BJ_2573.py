import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [[0]*(m+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ice = []
ice_around = [[4 for _ in range(m+2)] for _ in range(n+2)]

for r in range(1, n+1):
    for c in range(1, m+1):
        if board[r][c]:
            ice.append((r,c))
            for i in range(4):
                ice_around[r+dr[i]][c+dc[i]] -= 1
ans = 0
while True:
    finish = False

    for i in range(len(ice)-1, -1, -1):
        r, c = ice[i]
        board[r][c] -= ice_around[r][c]

    for i in range(len(ice)-1, -1, -1):
        r, c = ice[i]
        if board[r][c] <= 0:
            ice.pop(i)
            board[r][c] = 0
            for j in range(4):
                ice_around[r+dr[j]][c+dc[j]] += 1

    que = deque()
    visited = [[False for _ in range(m+2)] for _ in range(n+2)]
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not visited[i][j] and board[i][j]:
                cnt += 1
                if cnt>1:
                    finish = True
                que.append((i,j))
                visited[i][j] = True
                while que:
                    r, c = que.popleft()
                    for k in range(4):
                        nr, nc = r+dr[k], c+dc[k]
                        if not visited[nr][nc] and board[nr][nc]:
                            visited[nr][nc] = True
                            que.append((nr,nc))
    ans += 1
    if finish or not ice: break
if finish: print(ans)
else: print(0)