information = {}

def solution(info, query):
    
    for i in info:
        tmp = i.split()
        makeIt(tmp, "", 0)
        
    for key, value in information.items():
        information[key] = sorted(value)
        
    answer = []
    for q in query:
        tmp = q.split()
        word = ""
        
        for s in tmp[:len(tmp)-1]:
            if s!="and":
                word += s
                
        if word not in information:
            answer.append(0)
            continue
            
        score = information[word]
        std = int(tmp[-1])
        l, r = 0, len(score)-1
        
        while l<=r:
            mid = (l+r)//2
            if std <= score[mid]:
                r = mid-1
            else:
                l = mid+1
                
        answer.append(len(score)-l)
        
    return answer

def makeIt(arr, word, i):
    
    if i==len(arr)-1:
        if word not in information:
            information[word] = []
        information[word].append(int(arr[i]))
        return 
    
    makeIt(arr, word+arr[i], i+1)
    makeIt(arr, word+"-", i+1)