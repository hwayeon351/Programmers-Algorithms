def solution(N, number):
    if number == N: return 1
    dp = [0, [N]]
    for i in range(2, 9):
        p_set = set([int(str(N)*i)])
        for j in range(1, i//2+1):
            for x in dp[j]:
                for y in dp[i-j]:
                    p_set.add(x+y)
                    p_set.add(x-y)
                    p_set.add(y-x)
                    p_set.add(x*y)
                    if y!=0: p_set.add(x//y)
                    if x!=0: p_set.add(y//x)
        if number in p_set:
            return i
        dp.append(p_set)
    return -1
