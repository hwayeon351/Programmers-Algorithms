from string import ascii_uppercase
from collections import defaultdict

def solution(msg):
    answer = []
    dic = defaultdict(int)
    i = 0
    for c in ascii_uppercase:
        i += 1
        dic[c] = i
    start = 0
    end = 0
    while True:
        word = msg[start:end+1]
        if dic[word] > 0:
            answer.append(dic[word])
            end += 1
            if end >= len(msg):
                break
        else:
            i += 1
            dic[word] = i
            start += (end-start)
            while True:
                end += 1
                if end >= len(msg) or dic[msg[start:end+1]] == 0:
                    end -= 1
                    break
    return answer
