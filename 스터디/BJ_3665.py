import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
ans = []

for _ in range(tc):
    n = int(input())
    rank = [0] + list(map(int, input().split()))

    nextOf = [set() for _ in range(n+1)]
    childCnt = [0]*(n+1)

    for i in range(1, n):
        childCnt[rank[i+1]] = i
        for j in range(i+1, n+1):
            nextOf[rank[i]].add(rank[j])

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if a in nextOf[b]: a, b = b, a
    
        nextOf[a].remove(b)
        nextOf[b].add(a)
        childCnt[b] -= 1
        childCnt[a] += 1
    
    que = deque()
    order = []

    for i in range(1, n+1):
        if childCnt[i] == 0:
            que.append(i)
            order.append(i)

    while que:
        now = que.popleft()
        for i in nextOf[now]:
            childCnt[i] -= 1
            if childCnt[i] == 0:
                que.append(i)
                order.append(i)

    if len(order) != n: ans.append("IMPOSSIBLE")
    else: ans.append(" ".join(map(str, order)))

print("\n".join(ans))