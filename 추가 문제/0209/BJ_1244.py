import sys

input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    sex, num = map(int, input().split())
    num-=1
    if sex==1:
        switch = num
        while s<n:
            switches[num] = 0 if switches[num]==1 else 1
            num+=num