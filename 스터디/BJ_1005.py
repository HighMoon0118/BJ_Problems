import sys
from collections import deque

input = sys.stdin.readline

ans = []

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    childOf = [list() for _ in range(n+1)]
    parentCnt = [0]*(n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        childOf[a].append(b)
        parentCnt[b] += 1
    w = int(input())
    que = deque()
    que.extend([i for i in range(1, n+1) if not parentCnt[i]])
    take = [0]*(n+1)
    total = 0
    while que:
        now = que.popleft()
        if now == w:
            break
        for child in childOf[now]:
            parentCnt[child] -= 1
            take[child] = max(take[child], take[now]+time[now])
            if not parentCnt[child]:
                que.append(child)
    ans.append(take[w]+time[w])
print("\n".join(map(str, ans)))