from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([[p, i] for i, p in enumerate(priorities)])
    while True:
        cur = queue.popleft()
        if len(queue) == 0: return answer+1
        p_list = [p[0] for p in queue]
        if cur[0] < max(p_list):
            queue.append(cur)
        else:
            answer += 1
            if location == cur[1]: return answer
