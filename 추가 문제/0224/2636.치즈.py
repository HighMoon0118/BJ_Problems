import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[-1]*(m+2)]+[[-1]+list(map(int, input().split()))+[-1] for _ in range(n)]+[[-1]*(m+2)]

def clear():
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j]:
                return False
    return True

def count_cheese():
    c = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j]:
                c +=1
    return c

def dfs(r, c):
    visited[r][c] = True
    if not visited[r+1][c] and not board[r+1][c]: dfs(r+1,c)
    if not visited[r][c+1] and not board[r][c+1]: dfs(r,c+1)
    if not visited[r-1][c] and not board[r-1][c]: dfs(r-1,c)
    if not visited[r][c-1] and not board[r][c-1]: dfs(r,c-1)

time = 0
while not clear():
    time += 1
    ans = count_cheese()
    visited = [[False for _ in range(m+2)] for _ in range(n+2)]
    dfs(1,1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] and (visited[i+1][j] or visited[i][j+1] or visited[i-1][j] or visited[i][j-1]):
                board[i][j] = 0
print(time)
print(ans)