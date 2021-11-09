import sys
sys.setrecursionlimit(200001)
input = sys.stdin.readline

def dfs(idx, o):
    global a
    
    order[idx] = o
    visit[idx] = num
    if not visit[friendOf[idx]]:
        dfs(friendOf[idx], o+1)
    elif visit[idx] == visit[friendOf[idx]]:
        a += o-order[friendOf[idx]]+1
    
ans = []
tc = int(input())
for _ in range(tc):

    n = int(input())

    friendOf = [0]+list(map(int, input().split()))
    visit = [0]*(n+1)
    order = [0]*(n+1)

    num = 1
    a = 0

    for i in range(1, n+1):
        if not visit[i]:
            dfs(i, 1)
            num += 1

    ans.append(str(n - a))
print("\n".join(ans))