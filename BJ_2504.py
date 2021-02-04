import sys

input = sys.stdin.readline

isRight = True
line = input().strip()

def makeAnswer(word):
    global isRight

    if len(word)==2:
        if word[0]=='(' and word[1]==')':
            return 2
        elif word[0]=='[' and word[1]==']':
            return 3
        else:
            isRight=False
            return 1

    s_count, b_count, index = 0, 0, 0

    for i, c in enumerate(word):
        if c=='(':
            s_count+=1
        elif c=='[':
            b_count+=1
        elif c==')':
            s_count-=1
        elif c==']':
            b_count-=1;
        if s_count==b_count==0:
            index=i+1
            break
        if s_count<0 or b_count<0:
            isRight=False
            return 1
    
    if s_count!=0 or b_count!=0:
        isRight=False
        return 1

    if index!=len(word):
        return makeAnswer(word[:index]) + makeAnswer(word[index:])
    elif word[0]=='(':
        return 2*makeAnswer(word[1:-1])
    elif word[0]=='[':
        return 3*makeAnswer(word[1:-1])

ans = makeAnswer(line)

if isRight: print(ans)
else: print(0)

    