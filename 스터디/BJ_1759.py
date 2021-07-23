import sys

input = sys.stdin.readline

l, c = map(int, input().split())

vowel = ['a', 'e', 'i', 'o', 'u']

alpha = list(input().split())
alpha.sort()
ans = []
def makeIt(idx, cnt, aList):

    if cnt == l:
        vCnt = 0
        for v in vowel:
            if v in aList:
                vCnt += 1
        if 0 < vCnt <= l-2:
            ans.append("".join(aList))
        return

    if idx == c:
        return
    aList.append(alpha[idx])
    makeIt(idx+1, cnt+1, aList)
    aList.pop(-1)
    makeIt(idx+1, cnt, aList)

makeIt(0, 0, list())
print("\n".join(ans))