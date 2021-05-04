defmake_it(index, num):
    if index==n-1: return 1

    if dp[index][num]>=0: return dp[index][num]

    result = 0
    if num > 0:
        result += make_it(index+1, num-1)
    if num < 9:
        result += make_it(index+1, num+1)

    dp[index][num] = result
    return result

n = int(input())
dp = [[-1]*10 for _ in range(n)]
ans = 0
for i in range(1, 10):
    ans += make_it(0, i)
print(ans%1000000000) 