import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def isSoSu(num):

    sqrt = int(num**(0.5)) + 1
    for i in range(2, sqrt):
        if num % i == 0:
            return False
    return True

def isDiffOne(num1, num2):
    cnt = 0
    for i in range(4):
        if num1[i] != num2[i]:
            cnt += 1
    if cnt == 1: return True
    return False

t = int(input())
answer = []

numbers = []
for i in range(1000, 10000):
    if isSoSu(i):
        numbers.append(i)

for _ in range(t):

    a, b = map(int, input().split())

    if a == b: answer.append("0"); continue

    que = [(0, -a)]
    while que:
        cnt, now = heappop(que)
        if -now == b: break
        for next in numbers:
            if next > -now and isDiffOne(str(next), str(-now)):
                heappush(que, (cnt+1, -next))

    if -now != b: answer.append("Impossible")
    else: answer.append(str(cnt))
    
print("\n".join(answer))