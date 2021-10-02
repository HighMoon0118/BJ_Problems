import sys


def makeIt(word):
    tmp = tree
    for i, c in enumerate(word):
        if not c in tmp: 
            ans.append("--"*i+c)
            tmp[c] = {}
        tmp = tmp[c]


input = sys.stdin.readline
n = int(input())

tree = {}
ans = []
info = []
for _ in range(n):
    info.append(input().split())
info.sort(key=lambda x: (x[1:], x[0]))

for i in range(n):
    makeIt(info[i][1:])
print("\n".join(ans))