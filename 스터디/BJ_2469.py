import sys

input = sys.stdin.readline

def play():
    for i in range(k):
        who = ord("A")+i
        d = 0
        while d < n:
            if i<k-1 and ladder[d][i]=="-":
                i += 1
            elif i>0 and ladder[d][i-1]=="-":
                i -= 1
            d += 1
        if ord(order[i]) != who:
            return False
    return True

def make_it(i):
    global ans
    if ans: return
    if i==k-1: 
        if play():
            ans = "".join(ladder[l])
        return

    if i==0 or ladder[l][i-1]=="*":
        ladder[l][i] = "-"
        make_it(i+1)
    ladder[l][i] = "*"
    make_it(i+1)

k = int(input())
n = int(input())
order = input().strip()

ladder = []
for i in range(n):
    ladder.append(list(input().strip()))
    if ladder[i][0] == "?": l = i

ans = ""
make_it(0)
if not ans: ans = "x"*(k-1)
print(ans)