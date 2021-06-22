def solution(n, arr1, arr2):
    
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i]|arr2[i])
    
    answer = []
    for num in arr3:
        tmp = ""
        for i in range(n-1, -1, -1):
            if num & (1<<i):
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer