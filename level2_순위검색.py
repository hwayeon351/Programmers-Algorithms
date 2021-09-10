from itertools import combinations
from collections import defaultdict
import operator
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        temp = i.split(" ")
        score = int(temp[-1])
        key = temp[:-1]
        for r in range(5):
            for c in combinations(key, r):
                c = "".join(c)
                info_dict[c].append(score)
    for key in info_dict.keys():
        info_dict[key].sort()
    for q in query:
        q = q.replace("-", "")
        temp = q.split(" and ")
        last = temp[-1].split(" ")
        temp[-1] = last[0]
        key = "".join(temp)
        score = int(last[-1])
        result = info_dict[key]
        left, right = 0, len(result)
        if right != 0:
            while left < right:
                mid = (left+right)//2
                if result[mid] < score:
                    left = mid+1
                else:
                    right = mid
        answer.append(len(result)-right)
    return answer
