import sys
sys.setrecursionlimit(20000000)
def make(w):
    #1.
    if len(w) == 0: return ""
    
    #2. u, v로 분리
    u = ""
    v = ""
    for i in range(len(w)):
        u += w[i]
        if u.count('(') == u.count(')'):
            break
    v = w[i+1:]

    #3. u 체크
    stack = []
    for c in u:
        if not stack:
            stack.append(c)
            continue
        if stack[-1] == "(": 
            if c == ")": stack.pop()
            else: stack.append(c)
        else: stack.append(c) 

    #3-1.
    if len(stack) == 0: 
        return u+make(v)
    
    #4-1.
    ans = "(" + make(v) + ")"
    for i in range(1, len(u)-1):
        if u[i] == "(": ans += ")"
        else: ans += "("
    return ans
    
def solution(p):
    answer = make(p)
    
    return answer
