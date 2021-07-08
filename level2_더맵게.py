import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if scoville[0] < K: return -1
        if scoville[0] < K:
            answer += 1
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        else: return answer
    return answer
