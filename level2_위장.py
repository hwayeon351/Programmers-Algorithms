from collections import Counter
from functools import reduce
def solution(clothes):
    kinds = Counter(list(zip(*clothes))[1]).values()
    return reduce(lambda x, y:x*(y+1), kinds, 1)-1
