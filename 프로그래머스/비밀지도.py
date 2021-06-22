def solution(str1, str2):
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    setStr1 = set()
    setStr2 = set()
    
    for i in range(len(str1)-1):
        if "A" <= str1[i] <="Z" and "A" <= str1[i+1] <= "Z":
            setStr1.add(str1[i:i+2])
    for i in range(len(str2)-1):
        if "A" <= str2[i] <="Z" and "A" <= str2[i+1] <= "Z":
            setStr2.add(str2[i:i+2])
    
    a = len(setStr1&setStr2)
    b = len(setStr1|setStr2)
    
    answer = int((a/b)*65536)
    
    return answer

print(solution("FRANCE", "french"))