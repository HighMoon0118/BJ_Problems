import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
total = sum(num)

graph = [list() for _ in range(n)]

for i in range(n):
    graph[i] = [j-1 for j in list(map(int, input().split()))[1:]]

def makeIt(idx, bit, tmp):

    if idx == n:
        another = total - tmp
        gap = abs(another - tmp)
        answer.append((gap, bit))
        return

    makeIt(idx+1, bit|(1<<idx), tmp+num[idx])
    makeIt(idx+1, bit, tmp)


def dfs1(idx):
    if visit[idx] or not bit&(1<<idx): return
    visit[idx] = 1
    for node in graph[idx]:
        dfs1(node)

def dfs2(idx):
    if visit[idx] or bit&(1<<idx): return
    visit[idx] = 1
    for node in graph[idx]:
        dfs2(node)


def check():
    for i in range(n):
        if not visit[i]: return False
    return True

answer = []
result = -1

makeIt(0, 0, 0)
answer.sort(key=lambda x: x[0])

for gap, bit in answer:
    visit = [0]*n
    cnt = 0

    for i in range(n):
        if bit&(1<<i) and not visit[i]:
            cnt += 1
            if cnt == 2: break
            dfs1(i)
    if cnt == 2: continue

    cnt = 0
    for i in range(n):
        if not bit&(1<<i) and not visit[i]:
            cnt += 1
            if cnt == 2: break
            dfs2(i)
    
    if cnt == 1:
        result = gap
        break
print(result)