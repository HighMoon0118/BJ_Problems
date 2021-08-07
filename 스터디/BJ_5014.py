import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

t = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

aDict = {}
bDict = {}

def makeIt(idx, mList, mDict, total, cnt, toggle):

    if idx == len(mList) or toggle==2:
        if cnt > 0:
            mDict[total] = mDict.get(total, 0) + 1
        return

    if(toggle==0): 
        makeIt(idx+1, mList, mDict, total+mList[idx], cnt+1, 1)
        makeIt(idx+1, mList, mDict, total, cnt, 0)
    if(toggle==1): 
        makeIt(idx+1, mList, mDict, total+mList[idx], cnt+1, 1)
        makeIt(idx+1, mList, mDict, total, cnt, 2)

makeIt(0, A, aDict, 0, 0, 0)
makeIt(0, B, bDict, 0, 0, 0)

ans = 0

for num, cnt in aDict.items():
    need = t-num
    ans += cnt*bDict.get(need, 0)

print(ans)