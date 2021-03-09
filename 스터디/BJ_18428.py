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
lines = []  # 학생을 볼 수 있는 복도 리스트

for r, c in teacher:
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        line = []
        while board[nr][nc] == "X":  # 빈공간이 아닐 때까지 탐색
            line.append((nr, nc))
            nr, nc = nr+dr[i], nc+dc[i]
        if board[nr][nc] == "S":  # 탐색이 끝난 지점이 학생이면 복도 리스트에 append
            lines.append(line)

lines.sort(key = lambda x: len(x))
count = 0
while lines and count<3:  # 남은 복도가 없거나 세번 지울때까지 반복
    now = lines[0]
    if len(now)==0: break  # 만약 복도의 길이가 0인경우 불가능하므로 break
    maxL = []
    for block1 in now:  # 해당 복도가 다른 복도들과 겹치는 지점이 있으면 tmp에 추가
        tmp = [0]
        for i in range(1, len(lines)): 
            for block2 in lines[i]:
                if block1==block2:
                    tmp.append(i)
                    break
        if len(maxL) < len(tmp):
            maxL = tmp
    for i in maxL[::-1]:  # 가장 많이 겹치는 복도들 삭제
        lines.pop(i)
    count += 1

if lines:
    print("NO")
else: print("YES")