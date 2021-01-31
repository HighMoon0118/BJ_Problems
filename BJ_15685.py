import sys

input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(101)] for _ in range(101)]

dxy = [(1,0), (0,-1), (-1,0), (0,1)]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    line = []
    line.append((x,y))
    line.append((x+dxy[d][0],y+dxy[d][1]))

    for i in range(g):
        tmp=[]
        for dx, dy in line:
            dx, dy = dy*-1, dx
            tmp.append((dx,dy))
        px = line[-1][0]-tmp[-1][0]
        py = line[-1][1]-tmp[-1][1]
        for j in range(len(tmp)-2,-1,-1):
            line.append((tmp[j][0]+px, tmp[j][1]+py))
    
    for i in range(len(line)):
        board[line[i][0]][line[i][1]]=1
        
count=0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1]and board[i+1][j] and board[i+1][j+1]:
            count+=1
print(count)