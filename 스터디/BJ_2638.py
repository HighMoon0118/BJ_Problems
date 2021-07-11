import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def fillOut(r, c):

    visit[r][c] = 1
    board[r][c] = -1

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and not visit[nr][nc] and (board[nr][nc] <= 0):
            fillOut(nr, nc)

def melt(r, c):
    cnt = 0
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and board[nr][nc] == -1: cnt += 1

    if cnt >= 2: 
        return True
    return False

def makeIt(r, c):

    if melt(r, c): board[r][c] = 0
    else: board[r][c] += 1

    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and board[nr][nc] == hour:
            makeIt(nr, nc)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

hour = 1
while True:
    finish = True

    visit = [[0]*m for _ in range(n)]
    fillOut(0, 0)

    for row in range(n):
        for col in range(m):
            if board[row][col] == hour:
                finish = False
                makeIt(row, col)
    if finish: break
    hour += 1

print(hour-1)