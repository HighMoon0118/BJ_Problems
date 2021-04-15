import sys

input = sys.stdin.readline

def make_it(word):
    global is_pattern

    if not word:  # 빈 문자열이 됐다면 제대로 된 패턴임
        is_pattern = True
        return

    if word.startswith("01"):  # 01로 시작할 때
        make_it(word[2:])
    elif word.startswith("100"):  # 100으로 시작할 때
        i = 3
        while i < len(word) and word[i] == "0":  # 1이 나올때까지 i+1
            i += 1
        if i == len(word):  # 1이나오지 않고 끝나게 되면 return(1은 무조건 한번 이상 나와야 하기때문)
            return
        j = i
        while j < len(word) and word[j] == "1":  # 0이 나올때까지 j+1
            j += 1

        if j == len(word) or j-i == 1:  # 0이 안나왔거나 1이 한번만 나온경우 재귀 ㄱㄱ
            make_it(word[j:])           # 100100 인 경우때문에 1이 한번만 나온 경우를 따로 분리함
        elif j == len(word)-1:  # 10010 인 경우 때문
            return
        else:
            word = word[j:] 
            if word[1] == "0": word = "1" + word  # 1001101 과 1001100 두 경우를 나누기 위함
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