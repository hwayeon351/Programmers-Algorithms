from collections import defaultdict
def solution(play_time, adv_time, logs):
    if play_time == adv_time: return '00:00:00'

    answer_sec = 0
    answer_total_sec = 0
    log = []
    #counter[sec] = sec ~ sec+1까지 1초 동안의 시청자 수
    counter = defaultdict(int)
    for l in logs:
        time = l.split('-')
        t1 = list(map(int, time[0].split(':')))
        t2 = list(map(int, time[1].split(':')))
        s1 = t1[0]*3600 + t1[1]*60 + t1[2]
        s2 = t2[0]*3600 + t2[1]*60 + t2[2]
        counter[s1] += 1
        counter[s2] -= 1
        log.append([s1, s2])
    log.sort()
    play_time = list(map(int, play_time.split(':')))
    play_sec = play_time[0]*3600 + play_time[1]*60 + play_time[2]
    adv_time = list(map(int, adv_time.split(':')))
    adv_sec = adv_time[0]*3600 + adv_time[1]*60 + adv_time[2]
    
    for sec in range(1, play_sec):
        counter[sec] += counter[sec-1]
        
    for sec in range(1, play_sec):
        counter[sec] += counter[sec-1]
    
    for i in range(adv_sec-1, play_sec):
        if i < adv_sec: total_sec = counter[i]
        else: total_sec = counter[i] - counter[i-adv_sec] 
        if total_sec > answer_total_sec:
            answer_total_sec = total_sec
            answer_sec = i
            
    answer_sec -= (adv_sec - 1)
    hh = str(answer_sec//3600).zfill(2)
    answer_sec %= 3600
    mm = str(answer_sec//60).zfill(2)
    ss = str(answer_sec%60).zfill(2)
    
    return hh+':'+mm+':'+ss
