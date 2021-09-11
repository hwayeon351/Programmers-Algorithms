from bisect import bisect_left, bisect_right
from collections import defaultdict

def get_range(start, end, lst):
    left = bisect_left(lst, start)
    right = bisect_right(lst, end)
    return right - left

def solution(words, queries):
    answer = []
    word_dict = defaultdict(list)
    rvs_word_dict = defaultdict(list)
    
    for w in words:
        word_dict[len(w)].append(w)
        rvs_word_dict[len(w)].append(w[::-1])
        
    for key in word_dict.keys():
        word_dict[key].sort()
        rvs_word_dict[key].sort()
        
    for q in queries:
        if q[0] == '?':
            q = q[::-1]
            start, end = q.replace('?', 'a'), q.replace('?', 'z')
            lst = rvs_word_dict[len(q)]
        else:
            start, end = q.replace('?', 'a'), q.replace('?', 'z')
            lst = word_dict[len(q)]
        answer.append(get_range(start, end, lst))
            
    return answer
