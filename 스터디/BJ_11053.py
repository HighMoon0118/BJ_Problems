import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

st = [num[0]]
for i in range(1, n):

    if st[-1] < num[i]:
        st += [num[i]]

    elif st[-1] > num[i]:

        l, r = 0, len(st)-1
        
        while l<r:
            m = (l+r)//2
            if st[m] < num[i]:
                l = m+1
            else: 
                r = m
       
        st[r] = num[i]

print(len(st))