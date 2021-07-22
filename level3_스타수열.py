from collections import Counter
def solution(a):
    answer = -1
    num_dict = Counter(a).most_common()
    for key, value in num_dict:
        if answer > 2*value: continue
        i = 0
        cnt = 0
        while i < len(a)-1 and cnt < 2*value:
            if a[i] == key:
                if a[i+1] != key:
                    cnt += 2
                    i += 2
                else:
                    i += 1
            else:
                if a[i+1] == key:
                    cnt += 2
                    i += 2
                else:
                    i += 1
        if cnt > answer: answer = cnt
    return answer
