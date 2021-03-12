import sys

input = sys.stdin.readline

def makeIt(startN, index):
    global count, ans

    if ans: return

    num[index] = startN
    
    if index == 0:
        count += 1
        if count == n:
            ans = "".join(map(str, num[:i+1]))
            finish: True
        return

    for j in range(index-1, startN):
        makeIt(j, index-1)


n = int(input())
num = [0 for _ in range(10)]
count, ans = 0, ""
for i in range(10):
    for j in range(i, 10):
        makeIt(j, i)
        if ans: break
    if ans: break

if ans: print(ans[::-1])
else: print(-1)