import sys

input = sys.stdin.readline
ans = [0 for _ in range(5)]
for i in range(5):
    num = list(map(int, input().split()))
    ans[i] = sum(num)
maxIdx = 0
for i in range(5):
    if ans[maxIdx]<ans[i]:
        maxIdx=i
print(maxIdx+1, ans[maxIdx])