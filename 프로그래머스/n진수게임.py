
s = "0123456789ABCDEF"

def toN(n, num):

    if num == 0:
        return "0"
    
    tmp = ""
    while num > 0:
        tmp = s[num % n] + tmp
        num = num // n
    return tmp

def solution(n, t, m, p):
    answer = ""
    tmp = ""
    
    for i in range(t*m):
        tmp += toN(n, i)
        
    for s in range(p-1, t*m, m):
        answer += tmp[s]

    return answer