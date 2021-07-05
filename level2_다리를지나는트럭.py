from collections import deque
def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    bridge = deque()
    t = 0
    while wait or bridge:
        t += 1
        for truck in bridge:
            truck[1] += 1
        if len(bridge) > 0:
            if bridge[0][1] == bridge_length+1:
                bridge.popleft()
        if len(wait) > 0:
            if len(bridge) == 0:
                bridge.append([wait.popleft(), 1])
            elif len(bridge) < bridge_length and bridge[-1][1] > 1 and sum(list(zip(*bridge))[0]) + wait[0] <= weight:
                bridge.append([wait.popleft(), 1])
    return t
