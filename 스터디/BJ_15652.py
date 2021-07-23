import sys

input = sys.stdin.readline
n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
ans = []

def makeIt(idx, cnt, tmp):
    
    if cnt==m:
        ans.append(tmp)
        return
    
    if idx == n:
        return

    makeIt(idx, cnt+1, tmp+str(num[idx])+" ")
    makeIt(idx+1, cnt, tmp)

makeIt(0, 0, "")
print("\n".join(ans))