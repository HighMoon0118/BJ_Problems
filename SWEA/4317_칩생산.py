
t = int(input())

def makeIt(row, col, bit, cnt):

    if col == w-1: return 0
    if row >= h-1:
        b = 0
        for r in range(h):
            if board[r][col+1]:
                b |= (1<<r)
        return cnt + makeIt(0, col+1, b, 0)
    
    if row == 0 and dp[col][bit] >= 0: return dp[col][bit]

    result = 0
    for r in range(row, h-1):
        if board[r][col]==0 and board[r+1][col]==0 and board[r][col+1]==0 and board[r+1][col+1]==0:
            board[r][col]=board[r+1][col]=board[r][col+1]=board[r+1][col+1] = 1
            result = max(result, makeIt(r+2, col, bit, cnt+1))
            board[r][col]=board[r+1][col]=board[r][col+1]=board[r+1][col+1] = 0
            
    result = max(result, makeIt(h, col, bit, cnt))
    if row == 0: dp[col][bit] = result
    return result



ans = []  
for tc in range(1, t+1):
    h, w = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    
    dp = [[-1 for _ in range(1<<h)] for _ in range(w)]
    b = 0
    for r in range(h):
        if board[r][0]:
            b |= (1<<r)
    
    ans.append(f"#{tc} {makeIt(0,0,b,0)}")

print("\n".join(ans))