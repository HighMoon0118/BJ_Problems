import sys


input = sys.stdin.readline

m, n, l = map(int, input().split())
M = list(map(int, input().split()))  # 사냥꾼 리스트
N = [list(map(int, input().split())) for _ in range(n)]  # 동물 리스트

animal = []
for x, y in N:
    
    tmp = l - y
    if tmp < 0: continue
    animal.append((x-tmp, x+tmp))  # 동물을 잡을 수 있는 x 범위

animal.sort(key=lambda x: x[0])  # 범위의 시작점이 작은 순으로 정렬
M.sort()  # 사냥꾼도 x가 작은 순으로 정렬
i = j = ans = 0 

while i<len(animal) and j<m:
    if animal[i][0] <= M[j] <= animal[i][1]:  # 만약 사냥꾼이 동물을 잡을수 있는 범위에 있으면 다음 동물로 넘어감
        i += 1
        ans += 1
    elif M[j] < animal[i][0]:  # 만약 사냥꾼이 동물 범위보다 작다면 다음 사냥꾼으로 넘어감
        j += 1
    elif animal[i][1] < M[j]:  # 만약 사냥꾼이 동물 범위보다 크다면 다음 동물로 넘어감
        i += 1
    
print(ans)