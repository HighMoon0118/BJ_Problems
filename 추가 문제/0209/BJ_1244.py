import sys

input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    sex, num = map(int, input().split())
    if sex==1:  # 남자일 때
        i = num-1
        while i < n:
            switches[i] = 0 if switches[i] else 1
            i+=num 
    else:  # 여자일 때
        l = r = num-1
        while 0 <= l and r < n:
            if switches[l] == switches[r]:
                switches[l] = switches[r] = 0 if switches[l] else 1
                l, r = l-1, r+1
            else:
                break
ans = ""
for i in range(1,n+1):
    ans += f"{switches[i-1]} "
    if i%20==0:
        ans += "\n"
print(ans)