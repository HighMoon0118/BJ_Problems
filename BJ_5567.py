import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

relate = [[] for _ in range(n+1)]
check = [-1 for _ in range(n+1)]
check[1]=0

for i in range(m):
    a, b = map(int, input().split())
    relate[a].append(b)
    relate[b].append(a)

def makeAnswer(friend, count):  # dfs로 풀었지만 bfs가 더 간단할 듯
    if count==2:
        return 0

    result = 0
    for i in relate[friend]:
        if check[i]==-1:
            check[i]=count+1
            result += 1+makeAnswer(i, count+1)
        elif count < check[i]:
            check[i]=count+1
            result += makeAnswer(i, count+1)
    return result

print(makeAnswer(1,0))