from itertools import permutations

def solution(n, weak, dist):
    answer = -1
    permu = list(set(permutations(dist, len(dist))))

    for i in range(len(weak)):
        for per in permu:
            visit = [0] * len(weak)
            check = 0
            friend = 0
            loc = i
            for f in per:
                friend += 1
                check += 1
                visit[loc] = 1
                new_loc = weak[loc] + f
                
                if new_loc >= n:
                    for j in range(len(weak)):
                        if not visit[j]:
                            if weak[loc] < weak[j] < n or 0 <= weak[j] <= new_loc - n:
                                visit[j] = 1
                                check += 1
                    if new_loc - n == weak[i] or check == len(weak): break
                    
                else:
                    for j in range(len(weak)):
                        if not visit[j]:
                            if weak[loc] < weak[j] <= new_loc:
                                visit[j] = 1
                                check += 1
                    if new_loc == weak[i] or check == len(weak): break
                    
                loc += 1
                if loc == len(weak): loc = 0
                while visit[loc]:
                    loc += 1
                    if loc == len(weak): loc = 0

            if check == len(weak):
                if answer == -1 or answer > friend: answer = friend

    return answer
