def solution(citations):
    citations.sort(reverse=True)
    for i, h in enumerate(citations):
        if i+1 < h: continue
        elif i+1 == h: return h    
        elif i+1 > h: return i
    return len(citations)
