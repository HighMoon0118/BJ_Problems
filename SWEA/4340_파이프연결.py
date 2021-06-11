
def makeIt(how, row, col, cnt):
    global result
    if cnt+2*n-2-row-col >= result:
        return

    if row == n-1 and col == n-1:
        if board[row][col] <= 2 and how == 3 or board[row][col] > 2 and how == 0:
            result = min(result, cnt)
        return
    
    if how == 0 or how == 2:
        if board[row][col] > 2:
            if col > 0 and not visit[row][col-1] and board[row][col-1]:
                visit[row][col-1] = 1
                makeIt(1, row, col-1, cnt+1)
                visit[row][col-1] = 0
            if col < n-1 and not visit[row][col+1] and board[row][col+1]:
                visit[row][col+1] = 1
                makeIt(3, row, col+1, cnt+1)
                visit[row][col+1] = 0
        elif how == 0:
            if row < n-1 and not visit[row+1][col] and board[row+1][col]:
                visit[row+1][col] = 1
                makeIt(0, row+1, col, cnt+1)
                visit[row+1][col] = 0
        elif how == 2:
            if row > 0 and not visit[row-1][col] and board[row-1][col]:
                visit[row-1][col] = 1
                makeIt(2, row-1, col, cnt+1)
                visit[row-1][col] = 0
    else:
        if board[row][col] > 2:
            if row > 0 and not visit[row-1][col] and board[row-1][col]:
                visit[row-1][col] = 1
                makeIt(2, row-1, col, cnt+1)
                visit[row-1][col] = 0
            if row < n-1 and not visit[row+1][col] and board[row+1][col]:
                visit[row+1][col] = 1
                makeIt(0, row+1, col, cnt+1)
                visit[row+1][col] = 0
        elif how == 1:
            if col > 0 and not visit[row][col-1] and board[row][col-1]:
                visit[row][col-1] = 1
                makeIt(1, row, col-1, cnt+1)
                visit[row][col-1] = 0
        elif how == 3:
            if col < n-1 and not visit[row][col+1] and board[row][col+1]:
                visit[row][col+1] = 1
                makeIt(3, row, col+1, cnt+1)
                visit[row][col+1] = 0


t = int(input())

ans = []

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    result = 2500
    makeIt(3, 0, 0, 1)
    ans.append(f"#{tc} {result}")
print("\n".join(ans))