import sys

input = sys.stdin.readline

n = input().strip()
length = len(n)
ans = 0
for i in range(1, len(n)):
    ans+=i*(10**i-10**(i-1))

num = int(n)
num -= 10**(length-1)
ans += (num+1)*length
print(ans)