word = input()

is_tag = False
ans = ""  # 최종적으로 만들 String
sub = ""  # 뒤집을 문자를 담을 String

for c in word:
    if c=="<" or c==">":
        if c=="<":  # 태그가 시작됐을 때
            ans += sub[::-1]  # 이전에 단어를 다뤘다면 저장
            sub = ""
            is_tag = True
        else:  # 태그가 끝났을 때
            is_tag = False
        ans += c
        continue
    
    if is_tag:  # 현재 태그를 다룰 때
        ans += c
    elif c==" ":  # 한 단어가 끝났을 때
        ans += sub[::-1] + c
        sub = ""
    else:  # 태그가 아닌 문자일 때
        sub += c
ans += sub[::-1]
print(ans)