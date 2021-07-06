import sys

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def makeIt(row, col):
    result = 0
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if 0<=nr<r and 0<=nc<c and not visit[ord(board[nr][nc])-ord('A')]:
            visit[ord(board[nr][nc])-ord('A')] = True
            result = max(result, 1 + makeIt(nr, nc))
            visit[ord(board[nr][nc])-ord('A')] = False

    return result


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
visit = [0]*26
visit[ord(board[0][0])-ord('A')] = True
ans = makeIt(0, 0)

print(ans+1)