#좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = []

def shoot_light(x, y, d, grid, visit, ans_visit):
    length = 0
    
    while True:
        nd = d
        if grid[y][x] == 'L':
            nd = (d-1+4)%4
        elif grid[y][x] == 'R':
            nd = (d+1+4)%4
            
        nx = x + dx[nd]
        if nx < 0: nx += len(grid[0])
        elif nx >= len(grid[0]): nx -= len(grid[0])
        
        ny = y + dy[nd]
        if ny < 0: ny += len(grid)
        elif ny >= len(grid): ny -= len(grid)
        
        if visit[nd][ny][nx] > 0 and length > 0:
            if visit[d][y][x] == 0:
                answer.append(length)
                visit[d][y][x] = length
            return
        
        length += 1
        visit[nd][ny][nx] = length
        x = nx
        y = ny
        d = nd
    
def solution(grid):
    ans_visit = [[[0]*len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    visit = [[[0]*len(grid[0]) for _ in range(len(grid))] for _ in range(4)]

    for d in range(4):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if visit[d][y][x] > 0: continue
                shoot_light(x, y, d, grid, visit, ans_visit)
    answer.sort()
    return answer
