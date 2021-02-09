import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n) :
    board.append(list(map(int, input().split())))
    for j in range(n) :
        if board[i][j]==9 : 
            board[i][j]=0
            sr, sc = i, j

dr = -1, 0, 0, 1
dc = 0, -1, 1, 0

def findFish(r, c, s) :
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c]=0
    que = PriorityQueue()
    que.put((0,r,c))
    while not que.empty() :
        d, row, col = que.get()
        if 0<board[row][col]<s : 
            return d, row, col
        for i in range(4) :
            nr, nc = row+dr[i], col+dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] :
                visited[nr][nc] = True
                if board[nr][nc]<=s :
                    que.put((d+1, nr, nc))

    return 0, 0, 0

size, ans, count = 2, 0, 0

while(True) :
    day, r, c = findFish(sr, sc, size)
    if day==0 : break
    board[r][c]=0
    ans+=day
    count+=1
    sr, sc = r, c
    if count==size : 
        size+=1
        count=0

print(ans)