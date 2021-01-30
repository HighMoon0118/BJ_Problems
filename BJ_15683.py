import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
cctv = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if 0<board[i][j]<6:
            cctv.append((board[i][j],i,j))

def count_blank(tmp) :
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count += 1
    return count

def look_at(tmp,r,c,*tv):
    for i in tv :
        if i==0:
            for a in range(c+1, m):
                if tmp[r][a]==0:
                   tmp[r][a]=-1
                elif tmp[r][a]==6:
                    break
        elif i==1:
            for a in range(r+1, n):
                if tmp[a][c]==0:
                    tmp[a][c]=-1
                elif tmp[a][c]==6:
                    break
        elif i==2:
            for a in range(c-1,-1,-1):
                if tmp[r][a]==0:
                    tmp[r][a]=-1
                elif tmp[r][a]==6:
                    break
        elif i==3:
            for a in range(r-1,-1,-1):
                if tmp[a][c]==0:
                    tmp[a][c]=-1
                elif tmp[a][c]==6:
                    break


que = deque()

def makeAnswer(i) :
    if i==len(cctv):
        tmp = copy.deepcopy(board)
        for index, how in enumerate(que) :
            num, r, c = cctv[index]
            if num==1:
                look_at(tmp,r,c,how)
            elif num==2:
                look_at(tmp,r,c,how,(how+2)%4)
            elif num==3:
                look_at(tmp,r,c,how,(how+1)%4)
            elif num==4:
                look_at(tmp,r,c,how,(how+1)%4,(how+2)%4)
            elif num==5:
                look_at(tmp,r,c,0,1,2,3)

        return count_blank(tmp)

    num = cctv[i][0]
    result=100
    if num==2:
        for how in range(2):
            que.append(how)
            result=min(result,makeAnswer(i+1))
            que.pop()
    else :
        for how in range(4):
            que.append(how)
            result=min(result,makeAnswer(i+1))
            que.pop()
            
    return result
        
ans = makeAnswer(0)
print(ans)
