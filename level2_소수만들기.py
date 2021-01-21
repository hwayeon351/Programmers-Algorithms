from itertools import combinations
from math import sqrt

def solution(nums):
    answer = 0
    combi = combinations(nums, 3)
    for c in combi:
        c_sum = sum(c)
        num = int(sqrt(c_sum))+1
        i = 1
        for i in range(2, num + 1):
            if c_sum % i == 0:
                break
        if i == num:
            answer += 1
    return answer
