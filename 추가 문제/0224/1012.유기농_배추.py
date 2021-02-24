import sys
from collections import deque

input = sys.stdin.readline

c = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer=[]

for _ in range(c) :
    m, n, k = tuple(map(int, input().split()))

    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k) :
        c, r = tuple(map(int, input().split()))
        board[r][c] = 1

    que = deque()
    ans=0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 1 :
                ans+=1
                que.append((i,j))
                while que :
                    r, c = que.popleft()
                    for k in range(4) :
                        nextR, nextC = r+dr[k], c+dc[k]
                        if 0<=nextR<n and 0<=nextC<m and board[nextR][nextC]==1 :
                            board[nextR][nextC]=2
                            que.append((nextR,nextC))
    print(ans)
