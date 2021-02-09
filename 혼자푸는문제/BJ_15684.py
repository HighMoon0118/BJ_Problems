import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

board = [ [0 for _ in range(n+1)] for _ in range(h)]

for _ in range(m) :
    a, b = map(int, input().split())
    board[a-1][b]=1

def check_board(row, col):
    for r in range(row, h):
        if board[r][col]==1:
            return check_board(r+1,col+1)
        if board[r][col-1]==1:
            return check_board(r+1,col-1)
    return col

ans=4

def makeAnswer(row, col, count, next):
    global ans

    finish=True
    for c in range(1,n+1):
        if c!=check_board(0,c):
            finish=False
            break
    if finish:
        ans=min(ans, count)
        return

    if ans<=count or count==3 or col==n:
        return

    cando=next
    for r in range(row,h):
        if cando and board[r][col-1]==board[r][col]==board[r][col+1]:
            board[r][col]=1
            makeAnswer(r+1, col, count+1, False)
            board[r][col]=0
        else : 
            cando=True
    makeAnswer(0,col+1,count,True)

makeAnswer(0,1,0,True)
if ans==4 : 
    print(-1)
else: 
    print(ans)