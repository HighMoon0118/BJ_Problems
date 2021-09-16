import sys
sys.setrecursionlimit(500000)

input = sys.stdin.readline

n = int(input())
tree = [list() for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [0]*(n+1)

ans = 0

def makeIt(idx, d):
    global ans
    
    visit[idx] = 1

    if d and len(tree[idx]) == 1:
        ans += d
        return

    for node in tree[idx]:
        if not visit[node]:
            makeIt(node, d+1)

makeIt(1, 0)

if ans%2: print("Yes")
else: print("No")