import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

if n==1:  # row의 크기가 1일 때
    count = 1
elif n==2:  # row의 크기가 2일 때
    count = min(4, (m+1)//2)
elif n>=3:  # row의 크기가 3 이상일 때
    if m<=6:  # column의 크기가 6이하이면 최대 4개까지만 가능(7이상이여야지 4방향 가능)
        count = min(4, m)
    else:
        count = m - 2  # column의 크기가 7 이상일 때 4방향을 다 움직이면 5개 방문, 그 이후로 column하나당 한개씩 방문 가능
        # m-(7-5) = m-2
print(count)