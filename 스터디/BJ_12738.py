import sys

input = sys.stdin.readline


n = int(input())
number = list(map(int, input().split()))

st = [number[0]]

for num in number[1:]:

    if st[-1] > num:

        l, r = 0, len(st)-1

        while l <= r:
            mid = (l+r)//2
            if st[mid] < num: l = mid + 1
            else: r = mid - 1

        st[l] = num

    elif st[-1] < num: st.append(num)
    
print(len(st))