import sys

input = sys.stdin.readline

def makeIt(r, c, count):
    if count == 6:
        ans.add("".join(tmp))
        return 
    if board[r+1][c]!=".":
        tmp[count] = board[r+1][c]
        makeIt(r+1, c, count+1)
    if board[r][c+1]!=".":
        tmp[count] = board[r][c+1]
        makeIt(r, c+1, count+1)
    if board[r-1][c]!=".":
        tmp[count] = board[r-1][c]
        makeIt(r-1, c, count+1)
    if board[r][c-1]!=".":
        tmp[count] = board[r][c-1]
        makeIt(r, c-1, count+1)

board = [["."]*7]+[["."]+list(input().split())+["."] for _ in range(5)]+[["."]*7]
tmp = ["" for _ in range(6)]
ans = set()
for i in range(1,6):
    for j in range(1,6):
        makeIt(i, j, 0)
print(len(ans))