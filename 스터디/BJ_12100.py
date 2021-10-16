import sys

input = sys.stdin.readline

def makeIt(board, count):
    global ans

    if count==5: 
        m = 0
        for r in range(n):
            for c in range(n):
                if m < board[r][c]: m=board[r][c]
        ans = max(ans, m)
        return
    
    tmp = [[0]*n for _ in range(n)]
    
    for r in range(n):
        index=0
        pre=0
        for c in range(n):
            if board[r][c]!=0:
                if pre!=0:
                    if pre==board[r][c]:
                        tmp[r][index]=board[r][c]*2
                        pre=0
                    else:
                        tmp[r][index]=pre
                        pre=board[r][c]
                    index += 1
                else: pre=board[r][c]
            
            if c==n-1 and pre!=0: tmp[r][index]=pre
            
    makeIt(tmp, count+1)

    tmp = [[0]*n for _ in range(n)]
    
    for r in range(n):
        index=n-1
        pre=0
        for c in range(n-1, -1, -1):
            if board[r][c]!=0:
                if pre!=0:
                    if pre==board[r][c]:
                        tmp[r][index]=board[r][c]*2
                        pre=0
                    else:
                        tmp[r][index]=pre
                        pre=board[r][c]
                    index -= 1
                else: pre=board[r][c]
            
            if c==0 and pre!=0: tmp[r][index]=pre
            
    makeIt(tmp, count+1)
    
    tmp = [[0]*n for _ in range(n)]
    
    for c in range(n):
        index=0
        pre=0
        for r in range(n):
            if board[r][c]!=0:
                if pre!=0:
                    if pre==board[r][c]:
                        tmp[index][c]=board[r][c]*2
                        pre=0
                    else:
                        tmp[index][c]=pre
                        pre=board[r][c]
                    index += 1
                else: pre=board[r][c]
            
            if r==n-1 and pre!=0: tmp[index][c]=pre
            
    makeIt(tmp, count+1)
    
    tmp = [[0]*n for _ in range(n)]
    
    for c in range(n):
        index=n-1
        pre=0
        for r in range(n-1, -1, -1):
            if board[r][c]!=0:
                if pre!=0:
                    if pre==board[r][c]:
                        tmp[index][c]=board[r][c]*2
                        pre=0
                    else:
                        tmp[index][c]=pre
                        pre=board[r][c]
                    index -= 1
                else: pre=board[r][c]
            
            if r==0 and pre!=0: tmp[index][c]=pre
            
    makeIt(tmp, count+1)

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
makeIt(board, 0)
print(ans)