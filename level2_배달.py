from collections import defaultdict, deque
def make_map(road, _map):
    for a, b, c in road:
        _map[a].append([b, c])
        _map[b].append([a, c])
        
def get_order(_map, N, K):
    answer = 1
    visit = [0]*(N+1)
    q = deque()
    visit[1] = 1
    
    for t, dis in _map[1]:
        if dis > K: continue
        if not visit[t]:
            visit[t] = dis
            answer += 1
        elif visit[t] > dis: visit[t] = dis
        q.append([t, dis, [1, t]])
        
    while q:
        now_t, now_dis, now_route = q.popleft()
        if not visit[now_t]:
            answer += 1
            visit[now_t] = now_dis
        for new_t, dis in _map[now_t]:
            if 0 < visit[new_t] < now_dis + dis: continue
            if new_t not in now_route and now_dis+dis <= K:
                now_route.append(new_t)
                q.append([new_t, now_dis + dis, now_route])
                now_route.pop()
            
    return answer  

def solution(N, road, K):
    _map = defaultdict(list)
    make_map(road, _map)
    
    return get_order(_map, N, K)
