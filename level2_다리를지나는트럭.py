from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    wait = deque(truck_weights)
    t = 0
    now_weight = 0
    while bridge:
        t += 1
        now_weight -= bridge.popleft()
        if wait:
            if now_weight + wait[0] <= weight:
                t_weight = wait.popleft()
                bridge.append(t_weight)
                now_weight += t_weight
            else:
                bridge.append(0)
    return t
