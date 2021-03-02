import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [["W"]*(m+2)]+[["W"]+(list(input().strip()))+["W"] for _ in range(n)]+[["W"]*(m+2)]

que = deque()
ans = 0
for r in range(1, n+1):
    for c in range(1, m+1):
        if board[r][c]=="L":
            visited = [[False for _ in range(m+2)] for _ in range(n+2)]
            que.append((r,c,0))
            visited[r][c]=True
            while que:
                row, col, count = que.popleft()
                if not visited[row+1][col] and board[row+1][col]=="L": 
                    visited[row+1][col] = True
                    que.append((row+1, col, count+1))
                if not visited[row][col+1] and board[row][col+1]=="L": 
                    visited[row][col+1] = True
                    que.append((row, col+1, count+1))
                if not visited[row-1][col] and board[row-1][col]=="L": 
                    visited[row-1][col] = True
                    que.append((row-1, col, count+1))
                if not visited[row][col-1] and board[row][col-1]=="L": 
                    visited[row][col-1] = True
                    que.append((row, col-1, count+1))
            ans = max(ans, count)
print(ans)