def solution(m, n, board):
    ans = 0

    mboard = [list(s) for s in board]
    
    while True:
        erase = set()
        
        for r in range(m-1):
            for c in range(n-1):
                if mboard[r][c]!=" " and mboard[r][c]==mboard[r+1][c]==mboard[r][c+1]==mboard[r+1][c+1]:
                    erase.add((r, c))
                    erase.add((r+1, c))
                    erase.add((r, c+1))
                    erase.add((r+1, c+1))
        if not erase:
            break
            
        for r, c in erase:
            mboard[r][c] = " "
            ans += 1
        
        for row in range(m-2, -1, -1):
            for col in range(n):
                r, c = row, col
                if mboard[r][c] != " " and mboard[r+1][c] == " ":
                    while r+1 < m and mboard[r+1][c] == " ":
                        mboard[r+1][c] = mboard[r][c]
                        mboard[r][c] = " "
                        r += 1
        
    return ans

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))