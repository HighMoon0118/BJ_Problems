import sys
sys.setrecursionlimit(100000)
def make_it(index, cnt):
    if index >= n:
        return 0

    if dp[index][cnt]>=0: return dp[index][cnt]

    if cnt<2:
        dp[index][cnt] = grape[index] + make_it(index+1, cnt+1)
    dp[index][cnt] = max(dp[index][cnt], make_it(index+1, 0))
    
    return dp[index][cnt]
    

n = int(input())
grape = [int(input()) for _ in range(n)]
dp = [[-1]*3 for _ in range(n)]
print(make_it(0,0))