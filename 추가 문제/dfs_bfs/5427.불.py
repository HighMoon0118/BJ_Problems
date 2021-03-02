import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    m, n = map(int, input().split())
    board = [["#"]*(m+2)]+[["#"]+list(input().strip())+["#"] for _ in range(n)]+[["#"]*(m+2)]
    time = [[0 for _ in range(m+2)] for _ in range(n+2)]
    que = deque()
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j]=="@":
                board[i][j]="."
                sr, sc = i, j
            elif board[i][j]=="*":
                que.append((i,j,1))
                time[i][j] = 1
    while que:
        r, c, t = que.popleft()
        if not time[r+1][c] and board[r+1][c]==".":
            time[r+1][c] = t+1
            que.append((r+1,c,t+1))
        if not time[r][c+1] and board[r][c+1]==".":
            time[r][c+1] = t+1
            que.append((r,c+1,t+1))
        if not time[r-1][c] and board[r-1][c]==".":
            time[r-1][c] = t+1
            que.append((r-1,c,t+1))
        if not time[r][c-1] and board[r][c-1]==".":
            time[r][c-1] = t+1
            que.append((r,c-1,t+1))
    que.append((sr, sc, 1))
    visited = [[False for _ in range(m+2)] for _ in range(n+2)]
    visited[sr][sc] = True
    success = False
    while que:
        r, c, t = que.popleft()
        if r==1 or r==n or c==1 or c==m:
            success = True
            break
        t += 1
        if not visited[r+1][c] and (t < time[r+1][c] or (board[r+1][c]=="." and not time[r+1][c])):
            visited[r+1][c] = True
            que.append((r+1,c,t))

        if not visited[r][c+1] and (t < time[r][c+1] or (board[r][c+1]=="." and not time[r][c+1])):
            visited[r][c+1] = True
            que.append((r,c+1,t))

        if not visited[r-1][c] and (t < time[r-1][c] or (board[r-1][c]=="." and not time[r-1][c])):
            visited[r-1][c] = True
            que.append((r-1,c,t))

        if not visited[r][c-1] and (t < time[r][c-1] or (board[r][c-1]=="." and not time[r][c-1])):
            visited[r][c-1] = True
            que.append((r,c-1,t))
            
    if not success:
        ans.append("IMPOSSIBLE")
    else:
        ans.append(str(t))
print("\n".join(ans))