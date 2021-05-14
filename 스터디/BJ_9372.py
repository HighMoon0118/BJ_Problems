import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    trip = [input() for _ in range(m)]
    ans.append(str(n-1))
print('\n'.join(ans))