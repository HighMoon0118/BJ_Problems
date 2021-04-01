import sys

tc = int(input())
ans = []

for _ in range(tc):
    n = int(input())
    diction = {}
    for _ in range(n):
        cloth, sort = input().split()
        diction[sort] = diction.get(sort, 1) + 1
    result = 1
    for v in diction.values():
        result *= v
    ans.append(str(result-1))
print("\n".join(ans))