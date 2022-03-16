def move_110(s):
    stack = []
    cnt = 0
    for c in s:
        stack.append(c)
        if c == '0' and stack[-3:] == ['1', '1', '0']:
            del stack[-3:]
            cnt += 1
    idx = -1
    for i in range(len(stack)):
        if stack[i] == '0':
            idx = i
    return "".join(stack[:idx+1]) + "110"*cnt + "".join(stack[idx+1:])
    
def solution(s):
    answer = []
    for ss in s:
        answer.append(move_110(ss))
        
    return answer
