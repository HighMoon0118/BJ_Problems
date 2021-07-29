import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board=[]
homes=[]
chickens=[]

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]==1:
            homes.append((i, j))
        elif board[i][j]==2:
            chickens.append((i,j))

dist=[[0 for _ in range(len(chickens))] for _ in range(len(homes))]

for i in range(len(homes)):
    for j in range(len(chickens)):
        dist[i][j]=abs(homes[i][0]-chickens[j][0])+abs(homes[i][1]-chickens[j][1])

check = [False for _ in range(len(chickens))]
ans=10001
def makeAnswer(start, count):
    global ans
    if count==m:
        d_min=[100 for _ in range(len(homes))]

        for i in range(len(chickens)):
            if check[i]:
                for j in range(len(homes)):
                    d_min[j]=min(d_min[j], dist[j][i])
        ans=min(ans, sum(d_min))
        return

    for i in range(start, len(chickens)):
        check[i]=True
        makeAnswer(i+1, count+1)
        check[i]=False

makeAnswer(0,0)
print(ans)

    