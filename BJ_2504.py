import sys

input = sys.stdin.readline

isRight = True
line = input().strip()

def makeAnswer(word):
    global isRight  # 괄호열이 올바른 괄호열인가?

    if len(word)==2:  # 괄호열의 길이가 2일 때
        if word=='()': return 2  # ()이면 리턴 2
        elif word=='[]': return 3  # []이면 리턴 3

    # 소괄호, 대괄호, 인덱스
    s_count, b_count, index = 0, 0, 0

    for i, c in enumerate(word):

        if c=='(': s_count+=1    # 여는 소괄호 +1
        elif c==')': s_count-=1  # 닫는 소괄호 -1
        elif c=='[': b_count+=1  # 여는 대괄호 +1
        elif c==']': b_count-=1  # 닫는 대괄호 -1

        if s_count==b_count==0:  # 소괄호, 대괄호 모두 짝이 맞으면
            index=i+1            # 인덱스 저장하고 break
            break
        if s_count<0 or b_count<0:  # 괄호의 개수가 음수면 break
            break
    
    if s_count!=0 or b_count!=0:  # for문을 끝까지 돌았는데 짝이 안맞으면 올바르지 않은 괄호열
        isRight=False
        return -1

    if index!=len(word): return makeAnswer(word[:index]) + makeAnswer(word[index:])  # 여러 괄호열로 이루어졌을 때
    elif word[0]=='(': return 2*makeAnswer(word[1:-1])  # 소괄호로 덮여있을 때
    elif word[0]=='[': return 3*makeAnswer(word[1:-1])  # 대괄호로 덮여있을 때

ans = makeAnswer(line)

if isRight: print(ans)
else: print(0)

    