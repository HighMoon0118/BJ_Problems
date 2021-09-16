import sys
import math

input = sys.stdin.readline

def makeIt(idx):
    global i

    if idx >= n: return

    makeIt(idx*2)
    tree[idx] = order[i]
    i += 1
    makeIt(idx*2+1)

k = int(input())
order = list(map(int, input().split()))

n = int(math.pow(2, k))
tree = [0]*n

i = 0
makeIt(1)
i = 1
while i<n:
    print(*tree[i: i+i])
    i *= 2
