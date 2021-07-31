import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

l = int(input())
move = {}
for _ in range(l):
    time, d = input().split()
    move[int(time)] = d

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
que = deque()
que.append((0, 0))

ans = 0

def makeIt(r, c, how, t):
    global ans
    ans = t
    nHow = how

    if t in move:
        if move[t] == "L": nHow = (how-1)%4
        else: nHow = (how+1)%4
        
    nr, nc = r+d[nHow][0], c+d[nHow][1]

    if 0<=nr<n and 0<=nc<n and board[nr][nc] != 2:

        if board[nr][nc] == 0:
            if que:
                tr, tc = que.popleft()
                board[tr][tc] = 0

        board[nr][nc] = 2
        que.append((nr, nc))
        makeIt(nr, nc, nHow, t+1)

makeIt(0,0,0,0)
print(ans+1)