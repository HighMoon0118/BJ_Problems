import sys

input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))
m = int(input())
city.sort()
l, r = 0, city[-1]

while l <= r:
    mid = (l+r) // 2

    total = 0
    for i in range(n):
        if city[i] > mid: 
            total += mid*(n-i)
            break
        total += city[i]
        
    if total <= m:
        l = mid +1
    else:
        r = mid - 1
print(r)