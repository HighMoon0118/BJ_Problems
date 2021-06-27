def solution(m, musicinfos):
    answer = []
    
    for a in range(len(musicinfos)):

        line = musicinfos[a]

        lines = line.split(",")
        
        time1 = lines[0].split(":")
        time2 = lines[1].split(":")
        
        during = (int(time2[0])*60 + int(time2[1])) - (int(time1[0])*60 + int(time1[1]))
        music = []
        i = 0
        while i < len(lines[3]):
            if i < len(lines[3])-1 and lines[3][i+1] == "#":
                music.append(lines[3][i:i+2])
                i += 2
            else:
                music.append(lines[3][i])
                i += 1
        totalMusic = ""
        idx = 0
        for i in range(during):
            totalMusic += music[idx]
            idx += 1
            if idx == len(music):
                idx = 0

        if len(m) <= len(totalMusic):
            idx = totalMusic.find(m)
            while idx > -1:
                if idx+len(m)==len(totalMusic) or idx+len(m) < len(totalMusic) and totalMusic[idx+len(m)] != "#":
                    answer.append((-during, a, lines[2]))
                    break
                else:
                    idx = totalMusic.find(m, idx+1)
    if not answer:
        return "(None)"
    answer = sorted(answer)
    return answer[0][2]