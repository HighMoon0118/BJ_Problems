def solution(s):
    answer = len(s)
    
    for i in range(1, (len(s)//2)+1):
        
        tmp = ""
        cnt = 1
        for j in range(0, len(s)-i, i):
            
            to = j+i
            
            if s[j:to] == s[to:to+i]: 
                cnt += 1
            else:
                if cnt>1: 
                    tmp += str(cnt)+s[j:to]
                else: 
                    tmp += s[j:to]
                cnt = 1
                
                
        if cnt>1:
            tmp += str(cnt)+s[to:]
        else:
            tmp += s[to:]
            
        answer = min(answer, len(tmp))
        
    return answer