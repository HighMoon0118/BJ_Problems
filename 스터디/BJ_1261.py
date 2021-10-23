import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(n)]
boomCnt = [[10000]*m for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
que = deque()
que.append((0, 0, 0))
ans = 10000
while que:
    r, c, boom = que.popleft()
    if r==n-1 and c==m-1:
        ans = min(ans, boom)
        continue
    for i in range(4):
        nr, nc = r+d[i][0], c+d[i][1]
        if 0<=nr<n and 0<=nc<m:
            tmp = boom
            if board[nr][nc] == 1: tmp += 1
            if boomCnt[nr][nc] > tmp:
                boomCnt[nr][nc] = tmp
                que.append((nr, nc, tmp))
    
print(ans)