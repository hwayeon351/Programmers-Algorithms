from math import ceil
def solution(n, stations, w):
    answer = 0
    power = w*2+1
    left = stations[0]-w
    right = stations[0]+w
    if left > 1:
        answer += ceil(left/power)
    left = right+1
    for s in stations[1:]:
        right = s+w
        if left < s-w:
            answer += ceil((s-w-left)/power)
        left = right+1
    if right < n:
        answer += ceil((n-right)/power)

    return answer
