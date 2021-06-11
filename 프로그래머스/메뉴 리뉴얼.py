def solution(orders, course):
    
    ans = [{} for _ in range(len(course))]
    words = [[s for s in word] for word in orders]
    for word in words:
        word = sorted(word)
        tmp = makeIt("".join(word), 0, "", course)
        
        for s in tmp:
            index = course.index(len(s))
            ans[index][s] = ans[index].get(s, 0)+1

    answer = []     
    for words in ans:
        maxL = max(words.values()) if words.values() else 0
        if maxL < 2: continue
        for word, cnt in words.items():
            if cnt == maxL:
                answer.append(word)
    answer.sort()
    return answer

def makeIt(word, index, tmp, course):  # 재귀말고도 단순 for문으로도 만들 수 있음
    
    if index == len(word):
        if tmp and len(tmp) in course:
            return [tmp]
        return []
    result = []
    result += makeIt(word, index+1, tmp+word[index], course)
    result += makeIt(word, index+1, tmp, course)
    return result