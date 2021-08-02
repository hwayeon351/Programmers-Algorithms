def check_slot(start, slots):
    end = start + 1000 - 1
    cnt = 0
    for s in slots:
        if s[0] <= end and s[1] >= start:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    slots = []
    for l in lines:
        y, s, t = l.split(" ")
        ss = s.split(":")
        end = int(ss[0])*3600000 + int(ss[1])*60000 + int(float(ss[2])*1000)
        start = end - int(float(t.split("s")[0])*1000) + 1
        slots.append([start, end])
    for s in slots:
        answer = max(answer, check_slot(s[0], slots), check_slot(s[1], slots))
    return answer
