import sys
sys.setrecursionlimit(2500)

input = sys.stdin.readline

def makeIt(row, col, how):
    global ans
    
    if board[row][col] == 0:
        ans += 1
        board[row][col] == 2

    nr, nc = row+d[how][0], col+d[how][1]

    if 0<=nr<n and 0<=nc<m:
        if board[nr][nc]==0:
            makeIt(nr, nc, (how+3)%4)
        else:
            if possible(row, col):
                makeIt(row, col, (how+3)%4)
            else:
                back = (how+3)%4
                nr, nc = row+d[back][0], col+d[back][1]
                if 0<=nr<n and 0<=nc<m and board[nr][nc] != 1:
                    makeIt(nr, nc, how)
                else:
                    return


def possible(row, col):
    for dr, dc in d:
        nr, nc = row+dr, col+dc
        if 0<=nr<n and 0<=nc<m and board[nr][nc]==0:
            return True
    return False

n, m = map(int, input().split())

r, c, dir = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

d = [(0, 0), (-1, 0), (0, 1), (1, 0)]

ans = 0

makeIt(r, c, dir)
print(ans)