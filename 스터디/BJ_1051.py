import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().strip())))

min_len = min(n, m)
finish = False
ans = 1
for i in range(min_len-1, 0, -1):  # 가장 큰 정사각형 먼저 체크, 정사각형을 찾으면 바로 break
    for r in range(n-i):
        for c in range(m-i):
            if board[r][c]==board[r+i][c]==board[r][c+i]==board[r+i][c+i]:
                ans = (i+1)**2
                finish = True
                break
        if finish: break
    if finish: break

print(ans)
