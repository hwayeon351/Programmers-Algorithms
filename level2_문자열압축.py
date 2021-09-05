def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        result = ""
        stack = []
        before = ""
        cnt = 1
        for c in s:
            if len(stack) < i: 
                stack.append(c)
            if len(stack) == i:
                now_s = "".join(stack)
                if before == now_s:
                    cnt += 1
                else:
                    if cnt == 1: 
                        result += before
                        before = now_s
                    else:
                        result += str(cnt) + before
                        cnt = 1
                        before = now_s
                stack.clear()
        if cnt > 1: result += str(cnt)
        result += before + "".join(stack)
        if len(result) < answer: answer = len(result)
    return answer
