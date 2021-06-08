def solution(rows, columns, queries):
    
    board = [[columns*r+c for c in range(1, columns+1)] for r in range(rows)]
    
    answer = []
    
    for sr, sc, er, ec in queries:
        answer.append(rotation(sr-1, sc-1, er-1, ec-1, board))
    
    return answer

def rotation(sr, sc, er, ec, board):
    
    minN = erased1 = board[sr][sc]
    erased2 = 0
    
    for c in range(sc+1, ec+1):
        erased2 = board[sr][c]
        board[sr][c] = erased1
        erased1 = erased2
        minN = min(minN, erased1)
    
    for r in range(sr+1, er+1):
        erased2 = board[r][ec]
        board[r][ec] = erased1
        erased1 = erased2
        minN = min(minN, erased1)
        
    for c in range(ec-1, sc-1, -1):
        erased2 = board[er][c]
        board[er][c] = erased1
        erased1 = erased2
        minN = min(minN, erased1)
        
    for r in range(er-1, sr-1, -1):
        erased2 = board[r][sc]
        board[r][sc] = erased1
        erased1 = erased2
        minN = min(minN, erased1)
    
    return minN