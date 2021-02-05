import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

que = PriorityQueue()
ans = []
for _ in range(n):
    next = int(input())
    if next!=0:
        que.put((abs(next),next))
    elif not que.empty():
        ans.append(que.get()[1])
    else:
        ans.append(0)
print("\n".join(map(str, ans)))