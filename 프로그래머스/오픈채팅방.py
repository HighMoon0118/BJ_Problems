def solution(record):
    
    toNickname = {}
    
    ans = []
    for sentence in record:
        
        infor = sentence.split()
        
        
        if infor[0] == "Change" or infor[0] == "Enter":
            toNickname[infor[1]] = infor[2]
        
        if infor[0] == "Enter":
            ans.append((infor[1], "님이 들어왔습니다."))
        elif infor[0] == "Leave":
            ans.append((infor[1], "님이 나갔습니다."))
    
    answer = [toNickname[uid]+sentence for uid, sentence in ans]
    
    return answer