import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

que = deque()
for _ in range(n):
    next = int(input())
    if next>0:
        que.append(next)
    else:
        que.pop()
print(sum(que))