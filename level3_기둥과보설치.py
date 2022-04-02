def impossible(answer):
    for x, y, a in answer:
        #기둥
        if a == 0:
            if (y == 0) or ([x, y, 1] in answer) or ([x-1, y, 1] in answer) or ([x, y-1, 0] in answer): continue
            return True
        #보
        else:
            if ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer) or ([x-1, y, 1] in answer and [x+1, y, 1] in answer): continue
            return True
        
    return False
    
def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        item = [x, y, a]
        #설치
        if b == 1:
            answer.append(item)
            if impossible(answer):
                answer.remove(item)
        #삭제
        elif item in answer:
            answer.remove(item)
            if impossible(answer):
                answer.append(item)
                
    return sorted(answer, key = lambda x:(x[0], x[1], x[2]))
