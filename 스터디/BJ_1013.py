import sys

input = sys.stdin.readline

def make_it(word):
    global is_pattern

    if not word:
        is_pattern = True
        return

    if word.startswith("01"):
        make_it(word[2:])
    elif word.startswith("100"):
        i = 3
        while i < len(word) and word[i] == "0":
            i += 1
        if i == len(word):
            return
        j = i
        while j < len(word) and word[j] == "1":
            j += 1
        
        if j == len(word) or j-i == 1:
            make_it(word[j:])
        elif j == len(word)-1:
            return
        else:
            word = word[j:]
            if word[1] == "0": word = "1" + word
            make_it(word)
        
        

t = int(input())
ans = []

for _ in range(t):
    word = input().strip()
    is_pattern = False
    make_it(word)
    if is_pattern:
        ans.append("YES")
    else:
        ans.append("NO")
print("\n".join(ans))