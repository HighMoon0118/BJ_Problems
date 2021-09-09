import sys

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def clearDot():
    for c in range(6):
        for r in range(10, -1, -1):
            if board[r][c] != '.':
                row = r
                while row < 11:
                    if board[row+1][c] != '.': break
                    else:row += 1
                board[r][c], board[row][c] = board[row][c], board[r][c]

def isDot():
    for r in range(12):
        for c in range(6):
            if board[r][c] != '.':
                return False
    return True

def dfs(row, col, color):
    if board[row][col] == color:
        dots.append((row, col))
        board[row][col] = '.'
    else: return
    
    for dr, dc in d:
        nr, nc = row+dr, col+dc
        if 0 <= nr < 12 and 0 <= nc < 6:
            dfs(nr, nc, color)

ans = 0
while True:
    isChanged = False
    for r in range(12):
        for c in range(6):
            if board[r][c] != '.':
                color = board[r][c]
                dots = []
                dfs(r, c, board[r][c])
                if len(dots) < 4:
                    for row, col in dots:
                        board[row][col] = color
                else: isChanged = True

    clearDot()
    if not isChanged: break
    ans += 1
    if isDot():break
print(ans)