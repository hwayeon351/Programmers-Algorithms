from itertools import permutations
def solution(user_id, banned_id):
    ans_set = set()
    permu = permutations(user_id, len(banned_id))
    for p in permu:
        check = True
        for i, user in enumerate(p):
            if not check: break
            if len(user) != len(banned_id[i]): 
                check = False
                break
            for u, b in zip(user, banned_id[i]):
                if b == '*' or b == u: continue
                check = False
                break
        if check: ans_set.add("".join(sorted(list(p))))
    return len(ans_set)
