import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

check_r = [False for _ in range(h+1)]
check_c = [False for _ in range(w+1)]

for _ in range(n):
    how, l = map(int, input().split())
    if how:
        check_c[l]=True
    else:
        check_r[l]=True

row = []
col = []
count = 0
for i in range(h+1):
    if check_r[i] or i==h:
        row.append(count)
        count=0
    count+=1
count = 0
for i in range(w+1):
    if check_c[i] or i==w:
        col.append(count)
        count=0
    count+=1
row.sort()
col.sort()

print(row[-1]*col[-1])