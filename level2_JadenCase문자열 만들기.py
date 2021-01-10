def solution(s):
    i = 0
    while i < len(s):
        if i==len(s)-1: return s
        if s[i] == " ":
            i += 1
            s = s[:i] + s[i].upper() + s[i+1:].lower()
        else:
            if i == 0: s = s[i].upper() + s[i+1:].lower()
            i += 1
    return s
