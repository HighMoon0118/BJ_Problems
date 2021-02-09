import sys

input = sys.stdin.readline
num = []
for _ in range(10):
    num.append(int(input()))

ans = 0
for i in range(0,10):
    tmp = ans+num[i]
    if abs(100-ans)>=abs(100-tmp):
        ans = tmp
    else: break

print(ans)