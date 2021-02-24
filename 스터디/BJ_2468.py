import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def makeAnswer(r, c):
    for _ in range(4):
        nr, nc = r+dr[_], c+dc[_]
        if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and board[nr][nc]>i:
            visited[nr][nc] = True
            makeAnswer(nr, nc)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
check = [False for _ in range(101)]
for i in range(n):
    for j in range(n):
        check[board[i][j]] = True
ans = 1
for i in range(1, 100):
    if check[i]:
        result = 0
        visited = [[False for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if not visited[r][c] and board[r][c] > i:
                    visited[r][c] = True
                    result += 1
                    makeAnswer(r, c)
        ans = max(ans, result)
print(ans)