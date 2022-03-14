def solution(a, b, g, s, w, t):
    answer = 0
    left = 0
    right = 10**14*4
    
    while left <= right:
        mid = (left+right)//2
        g_sum, s_sum, total = 0, 0, 0
        for gold, silver, weight, time in zip(g, s, w, t):
            cnt = mid//(time*2)
            if mid % (time*2) >= time: cnt += 1
            
            new_gold = gold if gold <= weight*cnt else weight*cnt 
            new_silver = silver if silver <= weight*cnt else weight*cnt
            g_sum += new_gold
            s_sum += new_silver
            total += new_gold+new_silver if new_gold+new_silver <= weight*cnt else weight*cnt
            
            if g_sum >= a and s_sum >= b and total >= a+b: break
        else:
            left = mid + 1
            continue
        answer = mid
        right = mid - 1
    
    return answer
