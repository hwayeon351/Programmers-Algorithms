from heapq import heappop, heappush
def solution(n, works):
    if sum(works)-n <= 0: return 0
    max_heap = []
    for w in works:
        heappush(max_heap, (-w, w))
    while n > 0:
        root = heappop(max_heap)[1] - 1
        heappush(max_heap, (-root, root))
        n-=1
    return sum([w[1]**2 for w in max_heap])
