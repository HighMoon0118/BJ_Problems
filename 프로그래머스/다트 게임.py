def solution(dartResult):
    score = [0,0,0]
    idx = 0
    bonus = 0
    i = 0
    while i < len(dartResult):
        
        if dartResult[i] == '*':
            score[idx-1] *= 2
            if idx > 1:
                score[idx-2] *= 2
        elif dartResult[i] == "#":
            score[idx-1] *= -1
        elif dartResult[i] == "S":
            idx += 1
        elif dartResult[i] == "D":
            score[idx] *= score[idx]
            idx += 1
        elif dartResult[i] == "T":
            score[idx] *= score[idx]*score[idx]
            idx += 1
        elif dartResult[i] == "1" and dartResult[i+1] == "0":
            score[idx] = 10
            i += 1
        else:
            score[idx] = int(dartResult[i])
        i += 1
    
    
    return sum(score)