def solution(progresses, speeds):
    answer = []
    last = 100-progresses[0]
    front = 0
    if last%speeds[0] == 0:
        front = last//speeds[0]
    else: front = last//speeds[0]+1
    cnt = 1
    for i in range(1, len(progresses)):
        last = 100 - progresses[i]
        day = 0
        if last%speeds[i]==0:
            day = last//speeds[i]
        else:
            day = last//speeds[i]+1
        if day <= front:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            front = day
    answer.append(cnt)
    return answer
