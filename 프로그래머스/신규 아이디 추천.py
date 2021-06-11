def solution(new_id):
    
    tmp = ''
    for s in new_id:
        if 'A'<=s<='Z':
            s = chr(ord(s)+32)
        if '0'<=s<='9' or 'a'<=s<='z'or s=='-' or s=='_' or s=='.':
            if s=='.' and (not tmp or tmp[-1] == '.'):
                continue
            tmp += s
    tmp = tmp.strip('.')
    if not tmp:
        tmp = 'aaa'
    elif len(tmp) < 3:
        tmp += tmp[-1]*(3-len(tmp))
    else:
        tmp = tmp[:15]
        tmp = tmp.strip('.')
    
    return tmp