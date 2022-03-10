def solution(line):
    point_x = []
    point_y = []
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a1, b1, c1 = line[i]
            a2, b2, c2 = line[j]
            if a1*b2 - a2*b1 == 0: continue
            x = (b1*c2-b2*c1)/(a1*b2-a2*b1)
            y = (a2*c1-a1*c2)/(a1*b2-b1*a2)
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                point_x.append(int(x))
                point_y.append(int(y))

    min_x, min_y = min(point_x), min(point_y)
    board = [['.']*(max(point_x)-min_x+1) for _ in range(max(point_y)-min_y+1)]
    
    for x, y in zip(point_x, point_y):
        ny = y-min_y
        nx = x-min_x
        board[ny][nx] = '*'
    
    answer = []
    for i in range(len(board)-1, -1, -1):
        answer.append("".join(board[i]))
        
    return answer
