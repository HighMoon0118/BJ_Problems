import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k) :
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for i in range(y1, y2) :
        for j in range(x1, x2) :
            board[i][j] = 1

que = deque()
dr = 0, 1, 0, -1
dc = 1, 0, -1, 0
ans = []

for i in range(n) :
    for j in range(m) :
        if board[i][j]==0 :
            count = 1
            board[i][j] = 1
            que.append((i,j))
            while que :
                r, c = que.popleft()
                for k in range(4) :
                    nR, nC = r+dr[k], c+dc[k]
                    if 0<=nR<n and 0<=nC<m and board[nR][nC]==0 :
                        count += 1
                        board[nR][nC] = 1
                        que.append((nR,nC))
            ans.append(count)

ans.sort()

print(len(ans))
print(" ".join(map(str,ans)))