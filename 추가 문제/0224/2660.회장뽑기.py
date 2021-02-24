import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a==-1: break
    board[a].append(b)
    board[b].append(a)
ans = [0 for _ in range(n+1)]
score_min = 100
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    que = deque()
    que.append((i,0))
    visited[i] = True
    while que:
        now, d = que.popleft()
        for next in board[now]:
            if not visited[next]:
                visited[next]=True
                que.append((next, d+1))
    score_min = min(score_min, d)
    ans[i]=d
answer = []
count = 0
for i in range(1, n+1):
    if ans[i]==score_min:
        count += 1
        answer.append(i)
print(score_min, count)
print(*answer)