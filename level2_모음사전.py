from itertools import product
def solution(word):
    dic = []
    for i in product(['', 'A', 'E', 'I', 'O','U'], repeat=5):
        str_i = "".join(list(i))
        dic.append(str_i)

    dic = sorted(list(set(dic)))
    return dic.index(word)
