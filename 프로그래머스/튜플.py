def solution(s):
    
    tSet = [set(line.split(",")) for line in s[2:len(s)-2].split("},{")]
    tSet.sort(key=lambda x:len(x))
    ans = [int(list(tSet[0])[0])]
    for i in range(1, len(tSet)):
        tmp = tSet[i] - tSet[i-1]
        ans.append(int(list(tmp)[0]))
    
    return ans