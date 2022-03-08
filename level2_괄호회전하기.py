from collections import deque
def solution(s):
    answer = 0
    str = deque(s)
    for _ in range(len(s)):
        str.append(str.popleft())
        stack = []
        i = -1
        while i < len(str)-1:
            i += 1
            if not stack:
                stack.append(str[i])
                continue
            if (str[i] == ']' and stack[-1] == '[') or (str[i] == ')' and stack[-1] == '(') or (str[i] == '}' and stack[-1] == '{'):
                stack.pop()
            else: stack.append(str[i])
        if not stack: answer += 1
    return answer
