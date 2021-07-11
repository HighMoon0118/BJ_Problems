import sys

A, B, C = map(int, input().split())

def makeIt(a, b, c):
    if visit[a][b][c]: return
    visit[a][b][c] = 1
    
    if a:
        if B-b >= a: makeIt(0, b+a, c)
        else: makeIt(a-B+b, B, c)
        if C-c >= a: makeIt(0, b, c+a)
        else: makeIt(a-C+c, b, C)

    if b:
        if A-a >= b: makeIt(a+b, 0, c)
        else: makeIt(A, b-A+a, c)
        if C-c >= b: makeIt(a, 0, c+b)
        else: makeIt(a, b-A+a, C)

    if c:
        if B-b >= c: makeIt(a, b+c, 0)
        else: makeIt(a, B, c-B+b)
        if A-a >= c: makeIt(a+c, b, 0)
        else: makeIt(A, b, c-A+a)



ans = []
visit = [[[0]*(C+1) for _ in range(B+1)] for _ in range(A+1)]
makeIt(0, 0, C)
for b in range(B+1):
    for c in range(C+1):
        if visit[0][b][c]:
            ans.append(c)
ans.sort()
print(*ans)