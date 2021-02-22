word = input()

alpha = [0 for _ in range(26)]
for c in word:
    alpha[ord(c)-ord("A")]+=1

ans = ["" for _ in range(len(word))]

i = 0
half = len(word)//2

while i < half:  # i : 0 ~ half
    for j in range(26):
        if alpha[j] > 1:  # 만약 2개 이상이면
            ans[i] = ans[len(word)-1-i] = chr(ord("A")+j)
            alpha[j] -= 2
            i += 1
            break
    else: break  # 2개 이상인 알파벳이 없으면 break

if i!=half:  # i가 중앙까지 오지 못했을 때
    print("I'm Sorry Hansoo")
else:
    if len(word)%2:  # 중앙까지 왔지만 길이가 홀수 일 때 입력
        for j in range(26):
            if alpha[j]:
                ans[i] = chr(ord("A")+j)
    print("".join(ans))