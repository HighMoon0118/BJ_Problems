word = input()

is_tag = False
ans = ""
sub = ""

for c in word:
    if c=="<" or c==">":
        if c=="<":
            ans += sub[::-1]
            sub = ""
            is_tag = True
        else:
            is_tag = False
        ans += c
        continue
    
    if is_tag:
        ans += c
    elif c==" ":
        ans += sub[::-1] + c
        sub = ""
    else:
        sub += c
ans += sub[::-1]
print(ans)