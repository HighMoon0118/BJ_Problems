import sys
sys.setrecursionlimit(200000)

def makeIt(inL, inR, postL, postR):
    global idx
    if inR < inL or postR < postL: return

    root = postOrder[postR]
    preOrder[idx] = root
    idx += 1

    mid = idx_of[root]
    cnt = mid-inL-1
    makeIt(inL, mid-1, postL, postL+cnt)
    makeIt(mid+1, inR, postL+cnt+1, postR-1)


input = sys.stdin.readline

n = int(input())
inOrder = tuple(map(int, input().split()))
postOrder = tuple(map(int, input().split()))

idx_of = [0]*(n+1)
for i in range(n):
    idx_of[inOrder[i]] = i

preOrder = [0]*n
idx = 0
makeIt(0, n-1, 0, n-1)
print(' '.join(map(str, preOrder)))