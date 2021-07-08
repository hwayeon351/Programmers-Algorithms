import heapq
def solution(jobs):
    answer, now, cnt = 0, 0, 0
    start = -1
    min_heap = []
    while cnt < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(min_heap, [j[1], j[0]])
        if len(min_heap) > 0:
            job = heapq.heappop(min_heap)
            start = now
            now += job[0]
            answer += (now-job[1])
            cnt += 1
        else: now += 1
    return answer//len(jobs)
