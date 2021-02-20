word = input()

alpha = [0 for _ in range(26)]
for c in word:
    alpha[ord(c)-ord("A")]+=1

ans = ["" for _ in range(len(word))]
i = 0
half = len(word)//2
while i < half:
    for j in range(26):
        if alpha[j] > 1:
            ans[i] = ans[len(word)-1-i] = chr(ord("A")+j)
            alpha[j] -= 2
            i += 1
            break
    else: break

if i!=half:
    print("I'm Sorry Hansoo")
else:
    if len(word)%2:
        for j in range(26):
            if alpha[j]:
                ans[i] = chr(ord("A")+j)
    print("".join(ans))