import sys

input = sys.stdin.readline


def makeIt(word):
    global ans
    if not word:
        ans = "SUBMARINE"
        return

    if word.startswith("100"):
        i = 3
        while i<len(word):
            if word[i] == "0": i += 1
            else: break

        if i == len(word): return  # 1000 일 경우 return

        j = i
        while i<len(word):
            if word[i] == "1": i += 1
            else: break

        if j+1!=i and i<len(word)-1 and word[i+1] == "0": makeIt(word[i-1:])  # 10011001 일 경우
        else: makeIt(word[i:]) # 100101 일 경우

    elif word.startswith("01"): makeIt(word[2:])

ans = "NOISE"

makeIt(input().strip())

print(ans)