import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    spot = [tuple(map(int, input().split())) for _ in range(n+2)]
    index = list(range(1, n+2))
    que = deque()
    que.append(0)
    while que:
        now = que.popleft()
        if now == n+1: break
        for next in index:
            if abs(spot[now][0]-spot[next][0])+abs(spot[now][1]-spot[next][1]) <= 1000:
                que.append(next)
                index.remove(next)
    if n+1 not in index:
        ans.append("happy")
    else:
        ans.append("sad")
print("\n".join(ans))