import sys
def zero(num):
    if num==1: return 0
    if num==0: return 1

    if dp0[num]: return dp0[num]

    dp0[num] = zero(num-1) + zero(num-2)
    return dp0[num]

def one(num):
    if num==1: return 1
    if num==0: return 0

    if dp1[num]: return dp1[num]

    dp1[num] = one(num-1) + one(num-2)
    return dp1[num]

input = sys.stdin.readline
t = int(input())

dp0 = [0]*41
dp1 = [0]*41
ans = []
for _ in range(t):
    n = int(input())
    ans.append(f"{zero(n)} {one(n)}")
print("\n".join(ans))