import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def makeBoard():
    for i in range(1, n+1):
        for j in range(1, n+1):
            diff = num[i]^num[j]
            count = 0
            for b in range(k):
                if diff&(1<<b):
                    count+=1
            if count==1:
                board[i][j]=1
                board[j][i]=1
            

n, k = map(int, input().split())
bits = [[]]+[list(map(int, input().strip())) for _ in range(n)]
num = [0]

for i in range(1, n+1):
    number = 0
    for j in range(k):
        number += bits[i][k-1-j]<<j
    num.append(number)

a, b = map(int, input().split())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
makeBoard()
que = deque()
check = [[False for _ in range(n+1)] for _ in range(n+1)]

order = [0 for _ in range(n+1)]
order[a]=1
que.append((a, 1))

while que:
    now, d = que.popleft()
    if now==b: break
    for i in range(1, n+1):
        if i!=a and not check[now][i] and board[now][i]:
            check[now][i] = check[i][now] = True
            order[i] = d+1
            que.append((i, d+1))
if not order[b]:
    print(-1)
else:
    ans = [b]
    i = b
    while i!=a:
        d -= 1
        for j in range(1, n+1):
            if check[i][j] and order[j]==d:
                ans.append(j)
                i = j
                break
    print(" ".join(map(str,ans[::-1])))