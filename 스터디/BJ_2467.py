import sys

n = int(input())
num = list(map(int, input().split()))

num.sort()
idx = 0
ans = []
while idx < n-1:
    if num[idx] >=0:
        ans.append((num[idx]+num[idx+1], num[idx], num[idx+1]))
        break

    std = num[idx]

    l, r = idx+1, n-1

    while l<r:
        mid = (l+r)//2

        if abs(std + num[l]) < abs(std + num[r]):
            r = mid
        else:
            l = mid + 1

    ans.append((abs(num[r]+std), num[idx], num[r]))
    idx += 1

ans.sort(key=lambda x: x[0])
print(ans[0][1], ans[0][2])