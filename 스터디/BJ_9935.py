import sys

input = sys.stdin.readline

word = input().strip()
boom = input().strip()

tmp = ['']*len(word)
idx = 0
cnt = 0

for i in range(len(word)):

    tmp[idx] = word[i]
    
    if tmp[idx] == boom[-1] and idx >= len(boom)-1:
        idx2 = idx - len(boom) + 1
        for j in range(len(boom)):
            if boom[j] == tmp[idx2]:
                if j == len(boom)-1:
                    idx -= len(boom)
            else: break
            idx2 += 1
    idx += 1

if idx == 0:
    print("FRULA")
else:
    print("".join(tmp[0:idx]))