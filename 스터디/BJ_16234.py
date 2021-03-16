import sys
from collections import deque

input = sys.stdin.readline



N, L, R = map(int, input().split())

board = [[201]*(N+2)]+[[201]+list(map(int, input().split()))+[201] for _ in range(N)]+[[201]*(N+2)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
finish = False
ans = 0
while True:
    finish = True
    que = deque()
    visited = [[False for _ in range(N+2)] for _ in range(N+2)]
    for rr in range(1, N+1):
        for cc in range(1, N+1):
            if not visited[rr][cc]:
                for i in range(4):
                    nr, nc = rr+dr[i], cc+dc[i]
                    if L <= abs(board[nr][nc]-board[rr][cc]) <= R:
                        finish = False
                        union = [(rr,cc)]
                        total = board[rr][cc]
                        que.append((rr,cc))
                        visited[rr][cc] = True
                        while que:
                            r, c = que.popleft()
                            for i in range(4):
                                nr, nc = r+dr[i], c+dc[i]
                                if not visited[nr][nc] and L <= abs(board[nr][nc]-board[r][c]) <= R:
                                    visited[nr][nc] = True
                                    union.append((nr, nc))
                                    total += board[nr][nc]
                                    que.append((nr, nc))

                        div = total//len(union)
                        for r, c in union:
                            board[r][c] = div
                        break
    if finish : break
    ans += 1
print(ans)