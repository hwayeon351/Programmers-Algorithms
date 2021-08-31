def solution(places):
    m1_x = [-1, 0, 1, 0]
    m1_y = [0, -1, 0, 1]
    m2_x = [0, -1, 1, -2, 2, -1, 1, 0]
    m2_y = [-2, -1, -1, 0, 0, 1, 1, 2]
    px = [[0], [0,-1], [0,1], [-1], [1], [-1,0], [1,0], [0]]
    py = [[-1], [-1,0], [-1,0], [0], [0], [0,1], [0,1], [1]]
    answer = []
    for room in places:
        check = True
        for y in range(5):
            for x in range(5):
                if room[y][x] == 'P':
                    #맨해튼 거리 1
                    for dx, dy in zip(m1_x, m1_y):
                        nx = x+dx
                        ny = y+dy
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if room[ny][nx] == 'P':
                                check = False
                                break
                    else:
                        #맨해튼 거리 2
                        for d in range(len(m2_x)):
                            nx = x+m2_x[d]
                            ny = y+m2_y[d]
                            if 0 <= nx < 5 and 0 <= ny < 5:
                                if room[ny][nx] == 'P':
                                    #파티션 체크
                                    for p in range(len(px[d])):
                                        p_x = x+px[d][p]
                                        p_y = y+py[d][p]
                                        if 0 <= p_x < 5 and 0 <= p_y < 5:
                                            if room[p_y][p_x] != 'X':
                                                check = False
                                                break
                        else: continue
            else: continue
        if check: answer.append(1)
        else: answer.append(0)
    return answer
