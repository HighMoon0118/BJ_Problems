import sys

input = sys.stdin.readline

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa > bb: uf[a] = bb
    else: uf[b] = aa

def dfs(r, c):
    board[r][c] = num
    if board[r+1][c]==1: dfs(r+1,c)
    if board[r][c+1]==1: dfs(r,c+1)
    if board[r-1][c]==1: dfs(r-1,c)
    if board[r][c-1]==1: dfs(r,c-1)

n, m = map(int, input().split())

board = [[0]*(m+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]

num = 2
for r in range(1, n+1):
    for c in range(1, m+1):
        if board[r][c] == 1:
            dfs(r, c)
            num += 1

link = []
for i in range(1, n+1):
    c = 1
    cnt = 0
    island = board[i][c]
    while c<=m:
        if board[i][c] == 0:
            cnt += 1
        elif island and island != board[i][c]:
            if cnt > 1: link.append((cnt, island, board[i][c]))
            island = board[i][c]
            cnt = 0
        else: 
            island = board[i][c]
            cnt = 0
        c += 1

for i in range(1, m+1):
    r = 1
    cnt = 0
    island = board[r][i]
    while r<=n:
        if board[r][i] == 0:
            cnt += 1
        elif island and island != board[r][i]:
            if cnt > 1: link.append((cnt, island, board[r][i]))
            island = board[r][i]
            cnt = 0
        else: 
            island = board[r][i]
            cnt = 0
        r += 1

uf = [i for i in range(num)]

link.sort(key = lambda x: x[0])
cnt = ans = 0
MAX = num-3
for d, a, b in link:
    if find(a) != find(b):
        union(uf[a], uf[b])
        cnt += 1
        ans += d
        if cnt == MAX: break

if cnt != MAX: print(-1)
else: print(ans)