def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            if i == ")": return False
            elif i == "(": stack.append(s)
        else:
            if i == "(": stack.append(s)
            elif i == ")": stack.pop()
    
    if len(stack) == 0: return True
    else: return False
