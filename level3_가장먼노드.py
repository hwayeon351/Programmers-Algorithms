from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(graph, start, distances):
    q = []
    heappush(q, [0, start])
    while q:
        cur_dis, cur_dest = heappop(q)
        if cur_dis > distances[cur_dest]: continue
        distances[cur_dest] = cur_dis
        for new_dest in graph[cur_dest]:
            dis = cur_dis + 1
            if dis < distances[new_dest]:
                distances[new_dest] = dis
                heappush(q, [dis, new_dest])
                
def solution(n, edge):
    distances = {node: float('inf') for node in range(1, n+1)}
    graph = defaultdict(set)
    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    dijkstra(graph, 1, distances)
    return list(distances.values()).count(max(distances.values()))
