def solution(number, k):
    stack = []
    if k == len(number)-1: return max(number)
    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
            continue
        if stack[-1] >= number[i]:
            stack.append(number[i])
            continue
        while stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
            if k==0:
                return "".join(stack) + number[i:]
        stack.append(number[i])
    return "".join(stack[:-1])
