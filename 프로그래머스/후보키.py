keys = []

def solution(relation):
    global keys
    
    answer = 0
    n = len(relation[0])
    makeKeys(0, 0, n)
    
    keys = sorted(keys, key = lambda x : len(x))
    i = 0
    while i < len(keys):

        key = keys[i]
        check = set()
        for j in range(len(relation)):
            tmp = ""
            for b in range(n):
                if b in key:
                    tmp += relation[j][b]
            check.add(tmp)

        if len(check) == len(relation):
            j = i+1
            while j<len(keys):
                if (key & keys[j]) == key:
                    keys.remove(keys[j])
                else:
                    j += 1
            i += 1
        else:
            keys.remove(key)
            
    return len(keys)

def makeKeys(index, bit , n):
    global keys
    
    if index == n:
        tmp = set()
        for i in range(n):
            if bit & (1<<i):
                tmp.add(i)
        keys.append(tmp)
        return
    
    makeKeys(index+1, bit | (1<<index), n)
    makeKeys(index+1, bit, n)