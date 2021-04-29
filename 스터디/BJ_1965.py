import sys

n = int(input())
num = list(map(int, input().split()))

st = [num[0]]
i = 1
while i<n:
    if st[-1] < num[i]:
        st.append(num[i])
    else:
        l, r = 0, len(st)-1
        while l<r:
            mid = (l+r)//2
            if st[mid] >= num[i]:
                r = mid
            else:
                l = mid+1
        st[l] = num[i]
    i+=1
print(len(st))