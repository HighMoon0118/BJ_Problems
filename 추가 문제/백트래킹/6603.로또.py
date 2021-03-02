import sys

input = sys.stdin.readline
def makeIt(s, c):
    if c==6:
        ans.append(" ".join(map(str, tmp)))
        return
    for i in range(s, len(num)):
        tmp[c] = num[i]
        makeIt(i+1, c+1)

tmp = [0 for _ in range(6)]
ans = []
while True:
    num = list(map(int, input().split()))
    if len(num)==1:
        break
    makeIt(1, 0)
    ans.append("")
print("\n".join(ans))