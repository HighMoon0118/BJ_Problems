import sys

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def dfs(row, col, dist):
    if dist==k:
        if row==1 and col==c:
            return 1
        return 0

    result = 0
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if not visited[nr][nc] and board[nr][nc] == ".":
            visited[nr][nc] = True
            result += dfs(nr, nc, dist+1)
            visited[nr][nc] = False
    return result

r, c, k = map(int, input().split())

board = [["T"]*(c+2)]+[["T"]+list(input().strip())+["T"] for _ in range(r)]+[["T"]*(c+2)]
visited = [[False for _ in range(c+2)] for _ in range(r+2)]
visited[r][1] = True
print(dfs(r, 1, 1))