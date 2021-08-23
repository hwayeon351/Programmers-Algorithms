def solution(gems):
    kinds = len(set(gems))
    g_dict = dict()
    answer = []
    start = 0
    end = 0
    differ = len(gems)
    while end < len(gems):
        if gems[end] not in g_dict:
            g_dict[gems[end]] = 1
        else:
            g_dict[gems[end]] += 1
        if len(g_dict) == kinds:
            while start <= end:
                if g_dict[gems[start]] - 1 > 0:
                    g_dict[gems[start]] -= 1
                    start += 1
                elif end - start < differ:
                    answer = [start, end]
                    differ = end-start
                    break
                else: break
        end += 1
                
    return [answer[0]+1, answer[1]+1]
