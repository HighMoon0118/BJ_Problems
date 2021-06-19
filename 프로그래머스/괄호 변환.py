def solution(p):
    if not p:
        return ""
    
    cnt = 0
    right = True
    for i in range(len(p)):
        s = p[i]
        if s == "(":
            cnt += 1
        elif s == ")":
            cnt -= 1
        
        if cnt < 0: 
            right = False
        if cnt == 0:
            break
    
    if not right:
        tmp = ""
        for s in p[1:i]:
            if s == "(":
                tmp += ")"
            else:
                tmp += "("
        return "(" + solution(p[i+1:]) + ")" + tmp
        
    return p[:i+1] + solution(p[i+1:])