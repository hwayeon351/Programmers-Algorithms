def solution(m, n, board):
    answer = 0
    dx = [0, 1, 1]
    dy = [-1, -1, 0]
    erase = set()
    set_b = set()
    map_b = [list(board[i]) for i in range(m)]  
    while True:
        #지울 블록 찾기
        erase.clear()
        for y in range(m-1, 0, -1):
            for x in range(0, n-1):
                now_b = map_b[y][x]
                if now_b == '0': continue
                set_b.clear()
                set_b.add((x, y))
                for d in range(3):
                    ny = y+dy[d]
                    nx = x+dx[d]
                    if map_b[ny][nx] == now_b:
                        set_b.add((nx, ny))
                        continue
                    break
                else:
                    erase.update(set_b)
        #지울 블록이 없는 경우
        if len(erase) == 0: return answer
        #블록 지우기
        answer += len(erase)
        e_list = list(erase)
        while e_list:
            x, y = e_list.pop()
            map_b[y][x] = '0'
            
        #블록 내리기
        for col in range(n):
            for i in range(m-2, -1, -1):
                if map_b[i][col] == '0':
                    continue
                for j in range(m-1, i, -1):
                    if map_b[j][col] == '0':
                        map_b[j][col], map_b[i][col] = map_b[i][col], map_b[j][col]
                        break  
    return answer
