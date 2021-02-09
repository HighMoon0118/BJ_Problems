import sys

input = sys.stdin.readline

n = int(input())
dist = []
visited = [[False for _ in range(101)] for _ in range(101)]
count=0
for _ in range(n):
    x, y = map(int, input().split())
    for r in range(y,y+10):
        for c in range(x,x+10):
            if not visited[r][c]:
                visited[r][c]=True
                count+=1
print(count)