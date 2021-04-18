import sys

input = sys.stdin.readline

def make_it(num):

    if num == 0:
        return 1
    elif num < 0:
        return 0
        
    if dp[num]: return dp[num]
    
    dp[num] = make_it(num-1) + make_it(num-2) + make_it(num-3)
    return dp[num]

dp = [0 for _ in range(11)]
ans = []
t = int(input())
for _ in range(1, t+1):
    ans.append(str(make_it(int(input()))))

print("\n".join(ans))