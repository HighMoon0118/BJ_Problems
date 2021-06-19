def solution(lines):
    
    times = []
    
    for line in lines:
        words = line.split()
        time = words[1].split(":")
        
        end = int(time[0])*3600000 + int(time[1])*60000 + int(float(time[2])*1000)
        
        start = end - int(float(words[2][:-1])*1000) + 1
        
        times.append((start, end+1000))
    
    times = sorted(times, key = lambda x : x[0])
    ans = 0
    for i in range(len(times)):
        cnt = 0
        for j in range(len(times)):
            if times[j][0] < times[i][1]:
                if times[i][1] <= times[j][1] :
                    cnt += 1
            else: break
        ans = max(ans, cnt)
    return ans