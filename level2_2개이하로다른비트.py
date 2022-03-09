def solution(numbers):
    answer = []
    for num in numbers:
        num = int(num)
        new_num = bin(num+1)[2:]
        bin_num = bin(num)[2:].zfill(len(new_num))
        cnt = 0

        for i in range(len(bin_num)):
            if bin_num[i] == new_num[i]: continue
            cnt += 1
            if cnt > 2: break
        else:
            answer.append(int(new_num, 2))
            continue
        new_num = new_num[:i] + bin_num[i:]
        answer.append(int(new_num, 2))

    return answer
