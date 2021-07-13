def dp(x, y, road):
    if x < 0 or y < 0 or road[y][x] == -1:
        return 0
    if road[y][x] > 0:
        return road[y][x]
    road[y][x] = dp(x-1, y, road) + dp(x, y-1, road)
    return road[y][x]
    
def solution(m, n, puddles):
    road = [[0]*m for i in range(n)]
    for x, y in puddles:
        road[y-1][x-1] = -1
    if road[n-2][m-1] == road[n-1][m-2] == -1: return 0
    road[0][0] = 1
    return dp(m-1, n-1, road)%1000000007
