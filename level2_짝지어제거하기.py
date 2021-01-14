def solution(s):
    stack = []
    if len(s) % 2 != 0 or len(s) == 0: return 0
    for c in s:
        if len(stack) == 0: stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else: stack.append(c)
    if len(stack) == 0: return 1
    else: return 0
