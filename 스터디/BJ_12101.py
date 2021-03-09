import sys

input = sys.stdin.readline

def makeIt(num, result):  # 순열
    global ans, count
    if count == k or num > n:
        return
    if num==n:
        count += 1
        if count == k:
            ans = result
        return
    for i in range(1, 4):
        makeIt(num+i, result+str(i)+"+")

n, k = map(int, input().split())
ans, count = "-1 ", 0
makeIt(0, "")
print(ans[0:len(ans)-1])