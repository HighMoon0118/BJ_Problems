import sys

input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
count = [0 for _ in range(n+1)]

for i in range(1, n+1):
    sx, sy, w, h = map(int, input().split())
    for c in range(sx, sx+w):
        for r in range(sy, sy+h):
            count[board[r][c]]-=1
            board[r][c]=i
            count[i]+=1
ans = []
for i in range(1, n+1):
    ans.append(count[i])
print("\n".join(map(str,ans)))