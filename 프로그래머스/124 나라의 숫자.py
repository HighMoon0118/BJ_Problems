def solution(n):
    answer = makeIt(n)
    
    return answer

def makeIt(n):
    
    if n==0: return ""
    n -= 1
    div = n//3
    mod = n%3
    if mod == 0: return makeIt(div) + "1"
    elif mod == 1: return makeIt(div) + "2"
    else: return makeIt(div) + "4"