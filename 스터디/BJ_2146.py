import sys
sys.setrecursionlimit(20000)
from collections import deque

input = sys.stdin.readline

def dfs(row, col):

    que.append((row, col, 0))
    board[row][col] = num

    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if 0<=nr<n and 0<=nc<n and board[nr][nc] == 1:
            dfs(nr, nc)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

ans = 10000
num = 2
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            que = deque()
            dfs(r, c)

            visit = [[0]*n for _ in range(n)]

            while que:
                row, col, cnt = que.popleft()
                if cnt == ans: break
                if board[row][col] and num != board[row][col]:
                    break
                for i in range(4):
                    nr, nc = row+dr[i], col+dc[i]
                    if 0<=nr<n and 0<=nc<n and not visit[nr][nc]:
                        visit[nr][nc] = 1
                        que.append((nr, nc, cnt+1))

            ans = min(ans, cnt)
            num += 1

print(ans-1)