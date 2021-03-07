import sys

input = sys.stdin.readline

n = int(input())
board = [["O"]*(n+2)]+[["O"]+list(input().split())+["O"] for _ in range(n)]+[["O"]*(n+2)]
teacher = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == "T":
            teacher.append((i, j))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
lines = []
for r, c in teacher:
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        line = []
        while board[nr][nc] == "X":
            line.append((nr, nc))
            nr, nc = nr+dr[i], nc+dc[i]
        if board[nr][nc] == "S":
            lines.append(line)

lines.sort(key = lambda x: len(x))
count = 0
while lines and count<3:
    now = lines[0]
    if len(now)==0: break
    maxL = []
    for block1 in now:
        tmp = [0]
        for i in range(1, len(lines)):
            for block2 in lines[i]:
                if block1==block2:
                    tmp.append(i)
                    break
        if len(maxL) < len(tmp):
            maxL = tmp
    for i in maxL[::-1]:
        lines.pop(i)
    count += 1

if lines:
    print("NO")
else: print("YES")