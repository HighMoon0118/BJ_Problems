import sys

input = sys.stdin.readline

n, k = map(int, input().split())

check = [ False for _ in range(n+1)]
count=0
finish=False
for i in range(2,n+1):
    for num in range(i, n+1, i):
        if not check[num]:
            check[num]=True
            count+=1
            if count==k:
                ans=num
                finish=True
                break
    if finish:
        break
print(ans)