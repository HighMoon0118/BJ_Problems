import sys
from collections import deque

input = sys.stdin.readline

def makeIt(idx, num, bit):
    global ans

    if num == m:
        que = deque()
        visit = [[0]*(n+2) for _ in range(n+2)]

        for i in range(len(virus)):
            if bit&(1<<i):
                que.append(virus[i])
                visit[virus[i][0]][virus[i][1]] = 1

        cnt = 0
        blank = 0
        while que:
            temp = deque()
            isAllVirus = True
            while que:
                r, c = que.popleft()
                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if not visit[nr][nc] and board[nr][nc]!=1:
                        visit[nr][nc] = 1
                        temp.append((nr, nc))
                        if board[nr][nc]==0: 
                            blank += 1
                            isAllVirus = False

            if blank == blankCnt:
                if not isAllVirus: cnt += 1
                ans = min(ans, cnt)
                break

            cnt += 1
            que = temp

        return
    
    if idx == len(virus):
        return

    makeIt(idx+1, num+1, bit|(1<<idx))
    makeIt(idx+1, num, bit)

n, m = map(int, input().split())

board = [[1]*(n+2)] + [[1]+list(map(int, input().split()))+[1] for _ in range(n)] + [[1]*(n+2)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
virus = []

blankCnt = 0

for r in range(1, n+1):
    for c in range(1, n+1):
        if board[r][c] == 2:
            virus.append((r, c))
        elif board[r][c] == 0:
            blankCnt += 1

ans = 2500
makeIt(0, 0, 0)

if ans != 2500: print(ans)
else: print(-1)