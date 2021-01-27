import sys

input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n) :
    word = input()
    check = [False for _ in range(26)]
    pre = word[0]
    isGroup = True
    for c in word :
        if pre!=c :
            if check[ord(pre)-ord('a')] :
                isGroup = False
                break
            else :
                check[ord(pre)-ord('a')] = True
        pre = c
    if isGroup : ans+=1

print(ans)