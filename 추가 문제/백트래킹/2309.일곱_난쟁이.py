import sys

input = sys.stdin.readline

def makeIt(s, c, total, bit):
    if ans or total>100:
        return
    if c==7:
        if total == 100:
            for i in range(9):
                if bit&(1<<i)>0:
                    ans.append(num[i])
        return
    for i in range(s, 9):
        makeIt(i+1, c+1, total+num[i], bit|(1<<i))
    
num = [int(input()) for _ in range(9)]
ans = []
makeIt(0, 0, 0, 0)
ans.sort()
print("\n".join(map(str, ans)))