def solution(m, musicinfos):
    musics = []
    m_time = len(m) - m.count('#')
    m = m.replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')

    for info in musicinfos:
        info = info.split(",")
        info[0] = info[0].split(":")
        info[1] = info[1].split(":")
        if int(info[1][1]) < int(info[0][1]):
            mins = int(info[1][1]) + 60 - int(info[0][1])
            hours = int(info[1][0]) - 1 - int(info[0][0])
        else:
            mins = int(info[1][1]) - int(info[0][1])
            hours = int(info[1][0]) - int(info[0][0])
        time = mins + hours*60
        info[3] = info[3].replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')
        musics.append([time, len(info[3]), info[2], info[3]])
        
    musics.sort(key = lambda x: -x[0])
    
    for time, length, title, score in musics:
        if time < m_time: continue
        if time <= len(score):
            if m in score[:time]: return title
            continue
        ptime = max(m_time, time)
        music = score * (ptime//len(score)+1)
        if m in music: return title
    
    return "(None)"
