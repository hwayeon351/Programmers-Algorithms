from collections import deque
def solution(n, t, m, timetable):
    suttle = [["09:00", 0, ""]]
    timetable.sort()
    #셔틀 운행 시간 구하기
    for i in range(1, n):
        hh, mm = divmod(t*i, 60)
        suttle.append([str(9+hh).zfill(2) + ":" + str(mm).zfill(2), 0, ""])
    #크루들 셔틀 태우기
    bus = 0
    for crew in timetable:
        if bus == len(suttle): break
        #현재 크루가 현재 셔틀 시간보다 이전에 도착한 경우, 
        if suttle[bus][0] >= crew:
            suttle[bus][1] += 1
            suttle[bus][2] = crew
            if suttle[bus][1] == m: bus += 1
            continue
        #현재 크루가 탈 수 있는 셔틀 시간을 찾아서 태우기
        bus += 1
        while bus < len(suttle):
            if suttle[bus][0] >= crew:
                suttle[bus][1] += 1
                suttle[bus][2] = crew
                break
            bus += 1
    #콘 태우기
    if suttle[-1][1] < m: return suttle[-1][0]
    hh = int(suttle[-1][2][:2])
    mm = int(suttle[-1][2][3:])
    if mm == 0: return str(hh-1).zfill(2)+":59"
    return str(hh).zfill(2) + ":" + str(mm-1).zfill(2)
