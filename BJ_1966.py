import sys

input = sys.stdin.readline

case = int(input())
ans=[]
for c in range(case):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))

    num = que[m]
    count = 1
    index = 0
    last = 0
    for i in range(9,num,-1):
        for j in range(index, len(que)):
            if que[j]==i:
                count+=1
                last=j

        for j in range(0, index):
            if que[j]==i:
                count+=1
                last=j  
        index=last
    if index<=m:
        for j in range(index,m):
            if que[j]==num:
                count+=1
    else :
        for j in range(index,len(que)):
            if que[j]==num:
                count+=1
        for j in range(0, m):
            if que[j]==num:
                count+=1

    ans.append(count)
print('\n'.join(map(str,ans)))