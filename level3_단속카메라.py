def solution(routes):
    routes.sort(key = lambda x:x[0], reverse = True)
    camera = routes[0][0]
    answer = 1
    for i in range(1, len(routes)):
        if camera in range(routes[i][0], routes[i][1]+1):
            continue
        camera = routes[i][0]
        answer += 1     
    return answer
