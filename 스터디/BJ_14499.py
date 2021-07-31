import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

how = list(map(int, input().split()))
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


dice = [0]*6

def left():
    tmp = dice[5]
    dice[5] = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = tmp

def right():
    tmp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = tmp

def up():
    tmp = dice[5]
    dice[5] = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[1]
    dice[1] = tmp

def down():
    tmp = dice[5]
    dice[5] = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = tmp


r, c = x, y
ans = []

for h in how:
    nr, nc = r+d[h][0], c+d[h][1]

    if nr<0 or n==nr or nc<0 or m==nc:
        continue

    if h==1: right()
    elif h==2: left()
    elif h==3: up()
    else: down()

    if board[nr][nc]: 
        dice[5] = board[nr][nc]
        board[nr][nc] = 0
    else: board[nr][nc] = dice[5]

    ans.append(dice[0])
    r, c = nr, nc
print("\n".join(map(str, ans)))