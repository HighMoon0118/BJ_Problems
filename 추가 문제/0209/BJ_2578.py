import sys

input = sys.stdin.readline

check = [[False for _ in range(6)] for _ in range(6)]
rows = set()
cols = set()
cross = set()

def check_row(row):
    for i in range(1, 6):
        if not check[row][i]:
            return False
    return True
def check_col(col):
    for i in range(1, 6):
        if not check[i][col]:
            return False
    return True
def check_cross(row, col, how):
    if how:
        for i in range(1, 6):
            if not check[i][i]:
                return False
    else:
        for i in range(1, 6):
            if not check[6-i][i]:
                return False
    return True

num = [[] for _ in range(26)]
for i in range(1, 6):
    for j, number in enumerate(map(int, input().split()), start=1):
        num[number].extend([i,j])
check_num = []
for i in range(5):
    check_num.extend(list(map(int, input().split())))
ans = 0
for i in range(25):
    r, c = num[check_num[i]]
    check[r][c] = True
    if r not in rows:
        if check_row(r):
            rows.add(r)
            ans+=1
    if c not in cols:
        if check_col(c):
            cols.add(c)
            ans+=1
    if r==c and 0 not in cross:
        if check_cross(r, c, True):
            cross.add(0)
            ans+=1
    if r+c==6 and 6 not in cross:
        if check_cross(r, c, False):
            cross.add(6)
            ans+=1
    if ans>=3:
        print(i+1)
        break