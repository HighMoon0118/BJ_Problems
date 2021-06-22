def solution(str1, str2):
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    arr1 = []
    arr2 = []
    
    for i in range(len(str1)-1):
        if "A" <= str1[i] <="Z" and "A" <= str1[i+1] <= "Z":
            arr1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if "A" <= str2[i] <="Z" and "A" <= str2[i+1] <= "Z":
            arr2.append(str2[i:i+2])
    
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    i = j = 0
    a = b = 0
    
    while i<len(arr1) or j<len(arr2):
        
        if i==len(arr1) or (j<len(arr2) and arr1[i] > arr2[j]):
            j += 1
        elif j==len(arr2) or (i<len(arr1) and arr1[i] < arr2[j]):
            i += 1
        elif arr1[i] == arr2[j]:
            a += 1
            i += 1
            j += 1
        b += 1
    
    if b==0:
        return 65536
    
    answer = int((a/b)*65536)
    
    return answer