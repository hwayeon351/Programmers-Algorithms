from heapq import heappush, heappop
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    hp = []
    for i in range(1, len(food_times)+1):
        heappush(hp,[food_times[i-1], i])
    eat = 0
    length = len(food_times)
    prev_eat = 0
    while True:
        if eat + (hp[0][0] - prev_eat)*length >= k: break
        now_eat = heappop(hp)[0]
        eat += (now_eat - prev_eat)*length
        length -= 1
        prev_eat = now_eat
    hp.sort(key = lambda x:x[1])
    k -= eat
    return hp[k%length][1]
