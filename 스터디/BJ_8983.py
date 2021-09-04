import sys


input = sys.stdin.readline

m, n, l = map(int, input().split())
M = list(map(int, input().split()))
N = [list(map(int, input().split())) for _ in range(n)]

animal = []
for x, y in N:
    
    tmp = l - y
    if tmp < 0: continue
    animal.append((x-tmp, x+tmp))

animal.sort(key=lambda x: x[0])
M.sort()
i = j = ans = 0

while i<len(animal) and j<m:
    if animal[i][0] <= M[j] <= animal[i][1]:
        i += 1
        ans += 1
    elif M[j] < animal[i][0]:
        j += 1
    elif animal[i][1] < M[j]:
        i += 1
    
print(ans)