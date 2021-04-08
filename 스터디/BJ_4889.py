import sys

input = sys.stdin.readline

def check(word):
    i = st = 0
    cnt = 0
    while i<len(word):
        if word[i] == "{":
            st += 1
        else:
            if st == 0:
                cnt += 1
                st = 1
            else:
                st -= 1
        i += 1
    return cnt + st//2

ans = []
tc = 0
while True:
    tc += 1
    word = input().strip()
    if word[0] == "-":
        print("\n".join(ans))
        break
    ans.append(f"{tc}. {check(word)}")