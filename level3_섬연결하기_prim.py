import math

def get_min_edge_island(islands, costs):
    min_cost = math.inf
    cost_idx = 0
    for i, cost in enumerate(costs):
        print(i, cost)
        #cycle check
        if cost[0] in islands and cost[1] in islands:
            continue
        #connection check
        if cost[0] in islands or cost[1] in islands:
            if cost[2] < min_cost: 
                min_cost = cost[2]
                cost_idx = i
    return cost_idx
            
def solution(n, costs):
    answer = 0
    graph = [[0]*n for i in range(n)]
    
    for c in costs:
        graph[c[0]][c[1]] = c[2]
        graph[c[1]][c[0]] = c[2]   
    print(graph)
    islands = {costs[0][0]}
    while len(islands) < n:
        cost_idx = get_min_edge_island(islands, costs)
        answer += costs[cost_idx][2]
        islands.update([costs[cost_idx][0], costs[cost_idx][1]])
    
    return answer
