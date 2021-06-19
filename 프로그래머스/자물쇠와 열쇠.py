def solution(key, lock):
    
    m = len(key[0])
    n = len(lock[0])
    l = n+2*(m-1)
    
    board = [[0]*l for _ in range(l)]
    for r in range(n):
        for c in range(n):
            board[m-1+r][m-1+c] = lock[r][c]
    
    possible = False
    
    
    for i in range(4):
        key = rotate(key, m)
        
        for r in range(m-1+n):
            for c in range(m-1+n):

                canFill, board = fillOut(key, board, m, r, c, 0, 2)
                if canFill:
                    if check(board, m, n):
                        possible = True
                        break
                canFill, board = fillOut(key, board, m, r, c, 2, 0)
                
            if possible: break
        if possible: break
    
    return possible

def rotate(key, m):
    tmp = [[0]*m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            tmp[c][m-1-r] = key[r][c]
    return tmp

def fillOut(key, board, m, row, col, fromNum, toNum):
    for r in range(m):
        for c in range(m):
            if board[row+r][col+c] == fromNum and key[r][c] == 1:
                board[row+r][col+c] = toNum
            elif board[row+r][col+c] and key[r][c]:
                return False, board
    return True, board

def check(board, m, n):
    for r in range(m-1, m-1+n):
        for c in range(m-1, m-1+n):
            if board[r][c] == 0:
                return False
    return True