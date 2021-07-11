from heapq import heappush, heappop
def solution(operations):
    answer = []
    heap = []
    for op in operations:
        if op[0] == "I":
            heappush(heap, int(op[2:]))
        elif heap:
            if op[2:] == "-1":
                heappop(heap)
            else:
                heap.remove(max(heap))
    if heap: return [max(heap), heap[0]]
    return [0, 0]
