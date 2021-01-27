import sys
from collections import deque

imput = sys.stdin.readline
dr = 0, 1, 1, 1, 0, -1, -1, -1
dc = 1, 1, 0, -1, -1, -1, 0, 1
ans = []

while(True) :
    m, n = map(int, input().split())

    if m == 0 : break

    board = []

    for i in range(n) :
        board.append(list(map(int, input().split())))

    count = 0
    que = deque()

    for i in range(n) :
        for j in range(m) :
            if board[i][j] :
                count+=1
                que.append((i,j))

                while que :
                    r, c = que.popleft()
                    for k in range(8) :
                        nR, nC = r+dr[k], c+dc[k]
                        if 0<=nR<n and 0<=nC<m and board[nR][nC] :
                            board[nR][nC]=0
                            que.append((nR,nC))
    ans.append(count)

print("\n".join(map(str, ans)))
