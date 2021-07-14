def solution(name):
    alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    i = 0
    cnt = 0
    name = list(name)
    joy = ['A']*len(name)
    if 'A' != name[0]: 
        cnt = min(alpha[name[0]]-alpha['A'], alpha['Z']-alpha[name[0]]+alpha['A'])
        joy[0] = name[0]
    loc = 0
    while joy != name:
        for i in range(1, len(name)//2+1):
            left = (len(name)+loc-i)%len(name)
            right = (len(name)+loc+i)%len(name)
            if joy[right] != name[right]:
                loc = right
                cnt += i
                break
            elif joy[left] != name[left]:
                loc = left
                cnt += i
                break
        cnt += min(alpha[name[loc]]-alpha['A'], alpha['Z']-alpha[name[loc]]+alpha['A'])
        joy[loc] = name[loc]
                
    return cnt
