import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num.sort()
total = 3000000000

for i in range(n-2):
    
    if 0 <= num[i]:
        if abs(num[i]+num[i+1]+num[i+2]) < total:
            ans = [num[i], num[i+1], num[i+2]]
        break

    l, r = i+1, n-1

    while l<r:
        tmp = num[i] + num[l] + num[r]
        if abs(tmp) < total:
            total = abs(tmp)
            ans = [num[i], num[l], num[r]]
        if tmp < 0:
            l += 1
        elif 0 < tmp:
            r -= 1
        else:
            break

    if total == 0:
        break
    
print(" ".join(map(str, ans)))