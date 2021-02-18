import sys

input = sys.stdin.readline

board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

finish = False
row, col = -1, -1
for i in range(19):  # 가로 탐색
    count = 1
    for j in range(18):
        if board[i][j]!=0 and board[i][j]==board[i][j+1]:
            count+=1
            if count==5 and (j==17 or board[i][j+1]!=board[i][j+2]):
                finish = True
                row, col = i+1, j-2
                break
        else: count=1
    if finish: break

for i in range(19):  # 세로 탐색
    count = 1
    for j in range(18):
        if board[j][i]!=0 and board[j][i]==board[j+1][i]:
            count+=1
            if count==5 and (j==17 or board[j+1][i]!=board[j+2][i]):
                finish = True
                row, col = j-2, i+1
                break
        else: count=1
    if finish: break

r, c = 18, 0
while r!=0 or c!=18:  # 오른쪽 아래 대각선 탐색
    rr, cc = r, c
    count = 1
    while rr!=18 and cc!=18:
        if board[rr][cc]!=0 and board[rr][cc]==board[rr+1][cc+1]:
            count+=1
            if count==5 and (rr==17 or cc==17 or board[rr+1][cc+1]!=board[rr+2][cc+2]):
                finish = True
                row, col = rr-2, cc-2
                break
        else : count=1
        rr+=1
        cc+=1
    if r>0: r-=1
    else: c+=1
    if finish: break

r, c = 18, 18
while r!=0 or c!=0:  # 왼쪽 아래 대각선 탐색
    rr, cc = r, c
    count = 1
    while rr!=18 and cc!=0:
        if board[rr][cc]!=0 and board[rr][cc]==board[rr+1][cc-1]:
            count+=1
            if count==5 and (rr==17 or cc==1 or board[rr+1][cc-1]!=board[rr+2][cc-2]):
                finish = True
                row, col = rr+2, cc
                break
        else : count=1
        rr+=1
        cc-=1
    if r>0: r-=1
    else: c-=1
    if finish: break


if row==-1: print(0)
elif board[row-1][col-1]==1:
    print(1)
    print(row, col)
else:
    print(2)
    print(row, col)