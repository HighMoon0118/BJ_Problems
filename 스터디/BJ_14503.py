import sys
sys.setrecursionlimit(2500)

input = sys.stdin.readline

def makeIt(row, col, how, cnt):
    global ans
    if board[row][col] == 0:
        ans += 1
        board[row][col] = 2

    nr, nc = row+d[how][0], col+d[how][1]
    nhow = (how+3)%4
    if board[nr][nc] == 0: makeIt(nr, nc, nhow, 0)
    elif cnt == 4:
        nr, nc = row+d[nhow][0], col+d[nhow][1]
        if board[nr][nc] == 1: return
        else: makeIt(nr, nc, how, 0)
    elif board[nr][nc]: makeIt(row, col, nhow, cnt+1)

n, m = map(int, input().split())

r, c, dir = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

ans = 0

makeIt(r, c, dir, 0)
print(ans)